from src.project.logger import logging
from src.project.exception import CustomException

from src.project.components.data_eval import Evalutate
from src.project.config.configmanager import ConfigManager
import sys


class EvaluePipeline:
    def __init__(self):
        pass
    
    def run(self):
        config = ConfigManager()
        config = config.EvaluteManager()
        evalute = Evalutate(config=config)
        evalute.Evalute()
        evalute.save_score()
        evalute.log_into_mlflow()

if __name__ == '__main__':
    
    try:
        eval_obj  = EvaluePipeline()
        eval_obj.run()
    except Exception as e:
        raise CustomException(e,sys)