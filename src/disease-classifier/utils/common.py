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



@ensure_annotations
def read_yaml(path_to_yaml:Path) -> Configbox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info("loaded yaml sucessfully")
            return configbox(content)
    except BoxValueError:
        raise ValueError('yaml is empty ')
    except Exception as e:
        raise e
    
    
@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
        logger.info("json is created")