from src.project.logger import logging
from src.project.exception import CustomException


import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path


from src.project.entity.entity_config import PreparedBasedModelConfig

from src.project.config.configmanager import ConfigManager



class PreparedModel:
    def __init__(self,config:PreparedBasedModelConfig):
        self.config = config
        
    def BaseModel(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape = self.config.params_image_size,
            include_top = self.config.params_include_top,
            weights = self.config.params_weights
        )
        self.save_model(path= self.config.base_model_path,model=self.model)
        
    @staticmethod
    def save_model(path:Path,model=tf.keras.Model):
        model.save(path)
    
    
    
    @staticmethod
    def _prepared_base_model(classess,freeze_all,learning_rate,model):
        if freeze_all:
            for layers in model.layers:
                model.trainable = False
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction  = tf.keras.layers.Dense(
            units = classess,
            activation = "softmax"
        )(flatten_in)
        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
            
        )
        
        full_model.compile(
                optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss = tf.keras.losses.CategoricalCrossentropy(),
                metrics = ['accuracy']
            )
            
        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.full_model = self._prepared_base_model(
            classess=self.config.params_classess,
            freeze_all=True,
            learning_rate=self.config.params_learning_rate,
            model=self.model
        )
        
        self.save_model(path=self.config.updated_base_model_path,model=self.full_model)
        
            
        
        
