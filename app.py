from yolo5_detection.logger import logging
from yolo5_detection.exception import AppException
from yolo5_detection.pipeline.training_pipeline import TrainPipeline
import sys



obj = TrainPipeline()
obj.run_pipeline()