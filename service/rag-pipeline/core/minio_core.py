from minio import Minio
from dotenv import load_dotenv
import abc
import os


class MinioCore(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_data(self, bucket_name, object_name, file_path) -> bytes: ...
