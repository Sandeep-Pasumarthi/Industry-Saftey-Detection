from src.configuration.aws_connector import S3Client


class SimpleStorageService:
    def __init__(self):
        s3_client = S3Client()
        self.s3_resource = s3_client.s3_resource
        self.s3_client = s3_client.s3_client
    
    def download_file(self, key: str, bucket_name: str, filename: str) -> None:
        bucket = self.s3_resource.Bucket(bucket_name)
        bucket.download_file(Key = key, Filename = filename)
