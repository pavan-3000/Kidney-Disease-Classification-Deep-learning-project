from src.project.logger import logging
from src.project.exception import CustomException


from pathlib import Path
from dataclasses import dataclass



@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass
class PreparedBasedModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: int 
    params_include_top: bool
    params_weights: str 
    params_classess: int


@dataclass
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int 
    params_batch_size: float
    params_is_arugmentation: bool
    params_image_size: list
    