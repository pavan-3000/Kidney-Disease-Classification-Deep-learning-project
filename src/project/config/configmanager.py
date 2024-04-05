from src.project.constants import *
from src.project.utils.common import read_yaml,create_directory

from src.project.entity.entity_config import DataIngestionConfig
from src.project.entity.entity_config import PreparedBasedModelConfig,TrainingConfig
import os

from src.project.logger import logging
from src.project.exception import CustomException

from pathlib import Path
import sys

class ConfigManager:
    try:
        
        def __init__(
            
              self,
              config_path = CONFIG_FILE_PATH,
              params_path = PARAMS_FILE_PATH):
            self.config = read_yaml(config_path)
            self.params = read_yaml(params_path)
            logging.info("read the yaml")
            
            create_directory([self.config.artifacts_root])
            logging.info('created artifact dictories')
            
        def get_ingesion_config(self) -> DataIngestionConfig:
            config = self.config.data_ingestion
            
            create_directory([config.root_dir])
            
            logging.info("created root directory")
            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            )
            
            return data_ingestion_config

        
        
    except Exception as e:
        raise CustomException(e,sys)
    
    
        
    def BaseModelManager(self) -> PreparedBasedModelConfig:
        try:
            config = self.config.prepare_base_model
            params = self.params
            
            create_directory([config.root_dir])
            
            get_base_model = PreparedBasedModelConfig(
                root_dir=config.root_dir,
                base_model_path=config.base_model_path,
                updated_base_model_path=config.updated_base_model_path,
                params_classess=params.CLASSESS,
                params_image_size=params.IMAGE_SIZE,
                params_include_top=params.INCLUDE_TOP,
                params_learning_rate=params.LEARNING_RATE,
                params_weights=params.WEIGHTS
            )
            
            return get_base_model
            
            
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def trainingManager(self)-> TrainingConfig:
        try:
            logging.info("trainig config starred")
            
            config = self.config.training
            base = self.config.prepare_base_model
            
            training_data = os.path.join(self.config.data_ingestion.unzip_dir,'kidney-ct-scan-image')
            
            create_directory([config.root_dir])
            
            training_config = TrainingConfig(
                root_dir=config.root_dir,
                trained_model_path=config.trained_model_path,
                training_data=training_data,
                updated_base_model_path=base.updated_base_model_path,
                params_batch_size= self.params.BATCH_SIZE,
                params_epochs=self.params.EPOCHS,
                params_image_size=self.params.IMAGE_SIZE,
                params_is_augmentation=self.params.AUGMENTATION
                
            )
            
            return training_config
        except Exception as e:
            raise CustomException(e,sys)
        
  
