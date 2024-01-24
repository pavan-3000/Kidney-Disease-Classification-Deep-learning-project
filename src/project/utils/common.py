import os
from box.exceptions import BoxValueError
import yaml
from src import logger
import json
import joblib
from ensure import ensure_annotations
from box import Configbox
from pathlib import Path 
from typing import Any  
import base64 
from src.logger import logging
import sys
from src.project.exception import CustomException



@ensure_annotations
def read_yaml(path_to_yaml:Path) -> Configbox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info("loaded yaml sucessfully")
            return Configbox(content)
    except Exception as e:
        raise CustomException(e,sys)
    
    
@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
        logger.info("json is created")
    

@ensure_annotations
def create_directory(path_dir:list,verbose=True):
    for path in path_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"created directory at {path}")



def decodeImage(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageintobase(croppedimagepath):
    with open(croppedimagepath,'rb') as f:
        return base64.b64encode(f.read())
