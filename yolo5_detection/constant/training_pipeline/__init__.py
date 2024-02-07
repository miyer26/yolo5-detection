#data ingestion constants 
ARTIFACTS_DIR : str = "artifacts"
DATA_INGESTION_DIR : str = "data_ingestion"
DATA_INGESTION_DATA_STORE_DIR : str = "data_store"
DATA_DOWNLOAD_URL : str = "https://drive.google.com/file/d/1HU8nQK-6CuKKZcUWjfeNKgR_-eEVsBFx/view?usp=sharing"

#data validation constants

DATA_VALIDATION_DIR_NAME = "data_validation"
DATA_VALIDATION_STATUS_FILE = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "test", "data.yaml"]


#model training constants
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NUMBER_OF_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 2