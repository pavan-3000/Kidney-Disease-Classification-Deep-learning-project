from src.project.logger import logging
from src.project.exception import CustomException
import sys


from src.project.entity.entity_config import PrepareBaseModelConfig

from src.project.config.configmanager import ConfigManager

from src.project.components.preparebasemode import PreparedBaseModel




class prepare_base_model_pipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        try:
            config = ConfigManager()
            base_config = config.get_prepare_basemodel()
            base_model = PreparedBaseModel(config=base_config)
            base_model.get_base_model()
            base_model.update_base_model()
            
        except Exception as e:
            raise CustomException(e,sys)