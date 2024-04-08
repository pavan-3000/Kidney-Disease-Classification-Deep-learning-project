from src.project.logger import logging
from src.project.exception import CustomException

from src.project.components.preparebasemode import PreparedModel
from src.project.config.configmanager import ConfigManager
import sys

class BasePipeline:
    def __init__(self):
        pass 
    
    def main(self):
        try:
            base_config = ConfigManager()
            base_config = base_config.BaseModelManager()
            base_model = PreparedModel(config=base_config)
            base_model.BaseModel()
            base_model.update_base_model()
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    try:
        
        logging.info("staring pareaed base model")
        base_obj = BasePipeline()
        base_obj.main()
        logging.info("base modle is completed")
    except Exception as e:
        raise CustomException(e,sys)