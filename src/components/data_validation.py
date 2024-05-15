from src.entity.config import DataValidationConfig
from src.entity.artifact import DataIngestionArtifact, DataValidationArtifact
from src.constants.training import *

import os


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, config: DataValidationConfig=DataValidationConfig()):
        self.config = config
        self.data_ingestion_artifact = data_ingestion_artifact

    def validate_files_folders(self):
        files_folders = os.listdir(self.data_ingestion_artifact.image_store_path)
        self.status = True

        for ff in files_folders:
            if ff not in self.config.required_files_folders:
                self.status = False
                break
    
    def create_status_file(self):
        os.makedirs(self.config.data_validation_dir, exist_ok=True)

        with open(self.config.validation_status_file, "x") as f:
            f.write(str(self.status))
    
    def run(self) -> DataValidationArtifact:
        self.validate_files_folders()
        self.create_status_file()
        artifact = DataValidationArtifact(self.status)
        return artifact
