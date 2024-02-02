import os, sys
import shutil
from yolo5_detection.logger import logging
from yolo5_detection.exception import AppException

from yolo5_detection.entity.config_entity import DataValidationConfig
from yolo5_detection.entity.artifacts_entity import (DataIngestionArtifact,
                                                     DataValidationArtifact)


class DataValidation:

    def __init__(self,
                 DataIngestionArtifact: DataIngestionArtifact,
                 DataValidationConfig: DataValidationConfig) -> DataValidationArtifact:
        try:

            self.data_store_dir = DataIngestionArtifact.data_store_path
            self.data_validation_config = DataValidationConfig

        except Exception as e:
            raise AppException(e, sys)
        

    def validate_all_files_exist(self):
        try:
            curr_validation_status = None
            validation_status = True

            data_store_files = os.listdir(self.data_store_dir)
            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)

            with open(self.data_validation_config.data_validation_status_dir, 'w') as f:
                pass  # Do nothing, just truncate the file

            for i, file in enumerate(self.data_validation_config.required_files_list):
                if file not in data_store_files:
                    curr_validation_status = False
                else:
                    curr_validation_status = True

                validation_status = validation_status and curr_validation_status
                
                with open(self.data_validation_config.data_validation_status_dir, "a") as f:
                        f.write(f"Validation status: {file}: {curr_validation_status}\n")

            return  validation_status
        
        except Exception as e:
            raise AppException(e, sys)
    
    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info("Entered Data Validation:")
        try:
            validation_status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(validation_status=
                                                              validation_status)

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)