from src.entity.config import DataIngestionConfig
from src.entity.artifact import DataIngestionArtifact
from src.constants.training import *
from src.aws.s3 import SimpleStorageService

import os
import zipfile


class DataIngestion:
    def __init__(self, config: DataIngestionConfig=DataIngestionConfig()):
        self.config = config
        self.s3 = SimpleStorageService()
    
    def download_zip_file(self) -> str:
        download_dir = self.config.data_ingestion_dir
        os.makedirs(download_dir, exist_ok=True)
        zip_file_path = os.path.join(download_dir, self.config.s3_data_file_name)
        self.s3.download_file(key=self.config.s3_data_file_name, bucket_name=DATA_INGESTION_S3_BUCKET_NAME, filename=zip_file_path)
        return zip_file_path
    
    def unzip_file(self, path: str) -> str:
        unzip_dir = self.config.image_store_dir
        os.makedirs(unzip_dir, exist_ok=True)
        zip_ref = zipfile.ZipFile(path, 'r')
        zip_ref.extractall(unzip_dir)
        zip_ref.close()
        return unzip_dir

    def run(self) -> DataIngestionArtifact:
        zip_file_path = self.download_zip_file()
        unzip_dir = self.unzip_file(zip_file_path)
        artifact = DataIngestionArtifact(zip_file_path, unzip_dir)
        return artifact
