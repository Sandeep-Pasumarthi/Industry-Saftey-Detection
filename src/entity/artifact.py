from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    data_zip_file_path:str
    image_store_path:str