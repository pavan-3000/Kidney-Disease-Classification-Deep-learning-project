import os
import zipfile
from src.project.logger import logging
from src.project.exception import CustomException
import sys

from src.project.config.configmanager import ConfigManager
from src.project.entity.entity_config import EvaluteConfig
from pathlib import Path
import tensorflow as tf
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from src.project.utils.common import save_json

class Evalutate:
    def __init__(self,config:EvaluteConfig):
        self.config = config
        
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
    
    
    @staticmethod
    def load_model(path: Path)-> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    
    def Evalute(self):
        try:
            self.model = self.load_model(self.config.model_path)
            self._valid_generator()
            self.score = self.model.evaluate(self.valid_generator)
            self.save_score()
            
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def save_score(self):
        scores = {"loss":self.score[0],"accuracy":self.score[1]}
        save_json(path=Path("scores.json"),data = scores)
        
    def log_into_mlflow(self):
        try:
            mlflow.set_registry_uri(self.config.mlflow_uri)
            tracking_url_type_store = urlparse(mlflow.get_artifact_uri()).scheme
            if mlflow.active_run() is not None:
                
            # End the current run if one is active
                mlflow.end_run()
            
            with mlflow.start_run():
                mlflow.log_params(self.config.all_params)
                mlflow.log_metrics(
                    {"loss":self.score[0],"accuracy":self.score[1]}
                )
                
                if tracking_url_type_store != "file":
                    mlflow.keras.log_model(self.mode,"model",registered_model_name="VGG16Model")
                else:
                    mlflow.keras.log_model(self.model,"model")
            
        except Exception as e:
            raise CustomException(e,sys)

