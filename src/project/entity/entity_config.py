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


