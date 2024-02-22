
#from src.project.pipeline.ingestion_pipeline import DataIngestionPipeline
from src.project.logger import logging 
from src.project.exception import CustomException
import sys

from src.project.pipeline.preprared_base_model_pipeline import BasePipeline
'''
try:
    logging.info("datas ingestonston stared")
    obj = DataIngestionPipeline()
    obj.main()
    logging.info("data ingestion completd")
        
except Exception as e:
    raise CustomException(e,sys)
'''



try:
    
    logging.info("staring pareaed base model")
    base_obj = BasePipeline()
    base_obj.main()
    logging.info("base modle is completed")
except Exception as e:
    raise CustomException(e,sys)