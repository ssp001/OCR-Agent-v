from core.minio_core import MinioCore


class MinioService:
    def __init__(self, client: MinioCore) -> MinioCore:
        self.client = client

    def get_docs(self, docs: bytes, filename: str) -> MinioCore:
        respones = self.client.get_data(docs, filename)
        return respones

    def post_docs(self, docs: bytes, filename: str) -> MinioCore:
        respones = self.client.post_data(docs, filename)
        return respones
