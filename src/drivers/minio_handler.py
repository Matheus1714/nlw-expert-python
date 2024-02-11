from minio import Minio
from minio.error import S3Error
import io
# from settings import MINIO_HOST, MINIO_ACCESS_KEY, MINIO_SECRET_KEY

class MinioHandler:
    def __init__(self) -> None:
        self.connection = Minio(
            "localhost:9000",
            access_key='secret',
            secret_key='secret123#M1920',
            secure=False  # Set secure=True para habilitar SSL/TLS
        )
    
    def upload(self, bucket_name: str, object_name: str, file_path: str) -> str:
        if not self.__has_bucket(bucket_name):
            self.__create_bucket(bucket_name)
        
        return self.connection.fput_object(
            bucket_name,
            object_name,
            file_path,
        )
    
    def __create_bucket(self, bucket_name: str):
        self.connection.make_bucket(bucket_name)
        print(f'Create bucket with name: {bucket_name}')
    
    def __has_bucket(self, bucket_name: str):
        return self.connection.bucket_exists(bucket_name)