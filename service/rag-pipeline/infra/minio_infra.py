from core.minio_core import MinioCore
from dotenv import load_dotenv
import minio
import os
from utils.logger_module import logger
load_dotenv()


class MinioClient(MinioCore):
    def __init__(self, client: minio):
        try:
            self._client = client.Minio(endpoint=os.getenv("MINIO_ENDPOINT"),
                                        access_key=os.getenv(
                                            "MINIO_ACCESS_KEY"),
                                        secret_key=os.getenv(
                                            "MINIO_SECRET_KEY"),
                                        secure=False)
            if self._client.bucket_exists(os.getenv("BUCKET_NAME")):

                logger.info("s3 bukket connetion sucessfull")
                return None
        except Exception as error:
            logger.error(f"{str(error)}")

    def get_pdf(self, bucket_name, object_name, file_path):
        self._client.fget_object(bucket_name, object_name, file_path)
        return file_path
