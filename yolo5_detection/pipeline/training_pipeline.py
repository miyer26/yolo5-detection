import sys
import os
from yolo5_detection.logger import logging
from yolo5_detection.exception import AppException
from yolo5_detection.components.data_ingestion import DataIngestion
from yolo5_detection.components.data_validation import DataValidation
from yolo5_detection.entity.config_entity import (DataIngestionConfig,
                                                  DataValidationConfig)
from yolo5_detection.entity.artifacts_entity import (DataIngestionArtifact,
                                                     DataValidationArtifact)

 
class TrainPipeline:
    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

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
        
    def start_data_validation(self, 
                              data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        logging.info("Entered Data Validation step of pipeline:")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact,
                self.data_validation_config
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            if data_ingestion_artifact:
                logging.info("Data validation complete")
                logging.info(f"Result saved in: {self.data_validation_config.data_validation_status_dir}")
                logging.info("Exiting validation...")
            
            return data_validation_artifact
        
        except Exception as e:
            raise AppException(e, sys) from e
    
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact
            )

        except Exception as e:
            raise AppException(e, sys) from e