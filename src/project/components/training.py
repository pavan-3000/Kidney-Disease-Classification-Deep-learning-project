import os
import zipfile
import sys
from src.project.logger import logging
from src.project.exception import CustomException
from pathlib import Path
from src.project.config.configmanager import ConfigManager 
from src.project.entity.entity_config import TrainingConfig
import tensorflow as tf


class Training:
    def __init__(self,config:TrainingConfig):
        self.config = config
        
    def get_base_model(self):
        try:
            logging.info("triningingin")
            self.model = tf.keras.models.load_model(
                self.config.updated_base_model_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
    
    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
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

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )
    
    @staticmethod
    def save_model(path:Path,model:tf.keras.Model):
        model.save(Path)
        
    def train(self):
        try:
            self.model.fit(
                self.train_generator,
                epochs = self.config.params_epochs,
                validation_data = self.valid_generator
            )
            
            self.save_model(path=self.config.trained_model_path,model=self.model)
        except Exception as e:
            raise CustomException(e,sys)
