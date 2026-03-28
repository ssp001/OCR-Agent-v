from core.minio_core import MinioCore
from utils.logger_module import logger
from minio import Minio
from minio.error import S3Error, MinioException
from typing import Any
import io


class MinioClient(MinioCore):
    def __init__(self, ip_adress: str, access_key: str | None = None, secret_key: str | None = None, security: bool | None = bool):
        try:
            self.client = Minio(endpoint=ip_adress,
                                access_key=access_key, secret_key=secret_key, secure=security)
            if self.client.list_buckets():
                logger.info(f"Minio client login sucess fully{ip_adress}")
                return None
            else:
                pass
        except MinioException as error:
            logger.error(f"{str(error)}")

    def get_data(self, docs: bytes, filename: str) -> Any:
        """get_data function used to get data from the S3 server ```get_data(docs=?)```"""
        try:
            # getting the docs from server
            resones = self.client.get_object("source-files", f"{filename}")
            logger.info(f"docs fetched succesfully{filename}")
            # docs decoding
            data_bytes = resones.read()
            return data_bytes.decode("utf-8")
        except MinioException as error:
            logger.error(f"{str(error)}")
        finally:
            logger.info("Minio data fetching opration compleate")
            resones.close()
            resones.release_conn()

    def post_data(self, docs: Any, filename: str) -> Any:
        try:
            self.client.put_object(
                bucket_name="source-files/",
                # The path and filename in MinIO
                object_name=f"folder/{filename}",
                data=io.BytesIO(docs),      # Wrap bytes in a stream
                length=len(),           # MinIO needs to know the size
                content_type="application/pdf"        # Optional: helps browsers identify the file
            )
            logger.info("bukket data post is sucessfull")
        except MinioException as error:
            logger.error(f"{str(error)}")
