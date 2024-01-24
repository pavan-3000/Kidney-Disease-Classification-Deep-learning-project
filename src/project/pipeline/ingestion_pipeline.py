from src.project.logger import logging
from src.project.exception import CustomException
import sys

from src.project.config.configmanager import DataIngestionManager
from src.project.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            
            config = DataIngestionManager()
            ingestion_config = config.get_ingesion_config()
            data_ingestion = DataIngestion(config=ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__ == "__main__":
    try:
        logging.info("datas ingestonston stared")
        obj = DataIngestionPipeline()
        obj.main()
        logging.info("data ingestion completd")
        
    except Exception as e:
        raise CustomException(e,sys)
    
    
    