from src.project.constants import *
from src.project.utils.common import read_yaml,create_directory

from src.project.entity.entity_config import DataIngestionConfig
from src.project.entity.entity_config import PrepareBaseModelConfig


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
    
    
    def get_prepare_basemodel(self) -> PrepareBaseModelConfig:
        try:
            config = self.config.prepare_base_model
            
            create_directory([config.root_dir])
            logging.info('created root_dir')
            
            
            prepare_base_model_config = PrepareBaseModelConfig(
                root_dir= Path(config.root_dir),
                base_model_path= Path(config.base_model_path),
                updated_base_model_path= Path(config.updated_base_model_path),
                params_image_size= self.params.IMAGE_SIZE,
                params_classes=self.params.CLASSES,
                params_weights=self.params.WEIGHTS,
                params_learning_rate=self.params.LEARNING_RATE,
                params_include_top=self.params.INCLUDE_TOP
            )
            
            return prepare_base_model_config
            
            
        except Exception as e:
            raise CustomException(e,sys)