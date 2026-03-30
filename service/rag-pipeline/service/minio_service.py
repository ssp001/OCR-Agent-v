from core.minio_core import MinioCore


class MinioService:
    def __init__(self, client: MinioCore):
        self._client = client

    def get_pdf(self, bucket_name, object_name, file_path):
        docs = self._client.get_data(bucket_name=bucket_name,
                                     object_name=object_name, file_path=file_path)
        return docs
