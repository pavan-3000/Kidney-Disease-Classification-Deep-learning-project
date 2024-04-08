from src.project.logger import logging
from src.project.exception import CustomException

from src.project.components.data_ingestion import DataIngestion
from src.project.config.configmanager import ConfigManager
import sys


class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    
    def main(self):
        try:
            logging.info("data ingestion")
            config = ConfigManager()
            config  = config.get_ingesion_config()
            ingestion = DataIngestion(config=config)
            ingestion.download_file()
            ingestion.extract_zip_file()
            
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    try:
        logging.info("datas ingestonston stared")
        obj = DataIngestionPipeline()
        obj.main()
        logging.info("data ingestion completd")
            
    except Exception as e:
        raise CustomException(e,sys)