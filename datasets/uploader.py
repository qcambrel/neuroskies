import os
import boto3

class S3Uploader:
    def __init__(self, bucket_name: str) -> None:
        self.s3: boto3.client = boto3.client(
            "s3",
            aws_access_key_id=os.environ.get["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
            region_name=os.environ.get("AWS_REGION")
        )
        self.bucket_name: str = bucket_name

    def upload_file(self, file_path: str, key: str) -> None:
        self.s3.upload_file(file_path, self.bucket_name, key)

    def upload_fileobj(self, file_obj: bytes, key: str) -> None:
        self.s3.upload_fileobj(file_obj, self.bucket_name, key)