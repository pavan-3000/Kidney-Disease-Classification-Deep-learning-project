import os
import zipfile
from src.project.logger import logging
from src.project.exception import CustomException

from src.project.config.configmanager import ConfigManager

import sys
import gdown



class DataIngestion:
    def __init__(self,config:ConfigManager):
        self.config = config
        
    def download_file(self) -> str:
        try:
            data = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logging.info(f"downloaded data {data} into file {zip_download_dir}")
            
            file_id = data.split("/")[-2]
            prefix = 'https://drive.google.com/uc?export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)
            logging.info(f"downliaded data from {data} into file {zip_download_dir}")
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
        
    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            
            with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            
                
        except Exception as e:
            raise CustomException(e,sys)