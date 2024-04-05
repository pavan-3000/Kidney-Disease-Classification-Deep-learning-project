from src.project.logger import logging
from src.project.exception import CustomException

from src.project.components.training import Training
from src.project.config.configmanager import ConfigManager
import sys


class TrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def start(self):
        config = ConfigManager()
        config = config.trainingManager()
        train = Training(config=config)
        train.get_base_model()
        train.train_valid_generator()
        train.train()