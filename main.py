from src.project.pipeline.ingestion_pipeline import DataIngestionPipeline
from src.project.logger import logging 
from src.project.exception import CustomException
import sys

try:
    logging.info("datas ingestonston stared")
    obj = DataIngestionPipeline()
    obj.main()
    logging.info("data ingestion completd")
        
except Exception as e:
    raise CustomException(e,sys)
    