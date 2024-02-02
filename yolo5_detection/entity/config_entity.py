import os
from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from yolo5_detection.constant.training_pipeline import *


@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = ARTIFACTS_DIR

training_pipeline_config : TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir : str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR
    )

    data_store_file_path : str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_DATA_STORE_DIR
    )

    data_download_url : str = DATA_DOWNLOAD_URL

@dataclass
class DataValidationConfig:

    data_validation_dir : str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME
    )

    data_validation_status_dir : str = os.path.join(
        data_validation_dir, DATA_VALIDATION_STATUS_FILE
    )

    required_files_list : List[str] = field(default_factory=lambda: DATA_VALIDATION_ALL_REQUIRED_FILES)
