from src.constants.training import *
from dataclasses import dataclass
from datetime import datetime

import os

TIME_STAMP = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


@dataclass
class TrainingPipelineConfig:
    pipeline = PIPELINE
    artifact_dir = os.path.join(ARTIFACT_DIR)


training_pipeline_config_obj = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir = os.path.join(training_pipeline_config_obj.artifact_dir, DATA_INGESTION_DIR_NAME)
    image_store_dir = os.path.join(data_ingestion_dir, DATA_INGESTION_IMAGE_STORE_DIR)
    s3_data_file_name = DATA_INGESTION_S3_DATA_FILE_NAME
