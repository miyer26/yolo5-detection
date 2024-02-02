import sys
import os
from yolo5_detection.logger import logging
from yolo5_detection.exception import AppException
from yolo5_detection.components.data_ingestion import DataIngestion
from yolo5_detection.entity.config_entity import DataIngestionConfig
from yolo5_detection.entity.artifacts_entity import DataIngestionArtifact

 
class TrainPipeline:
    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Starting data ingestion...")

            data_ingestion = DataIngestion()
            data_ingestion_artifact = data_ingestion.initate_data_ingestion()
            logging.info("Download and extraction complete")
            logging.info("Exited data_ingestion step in TrainPipeline")

            return data_ingestion_artifact
        
        except Exception as e:
            raise AppException(e, sys)
        
    
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise AppException(e, sys) from e