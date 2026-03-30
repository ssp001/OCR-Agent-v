from utils.logger_module import logger
from core.vector_store_core import VectorStoreCore
from langchain_community.vectorstores import FAISS


class VectorStoreMethod(VectorStoreCore):
    def __init__(self, embedding, docs, kwargs: int):
        self.store = FAISS.from_texts(embedding, docs)
        self._kwargs: int = kwargs

    def store_and_search(self, query: str):
        try:
            respones = self.store.similarity_search(query, k=self._kwargs)
            logger.info("your data is stored sucessfuly")
            return respones
        except Exception as error:
            logger.error(error)
            raise RuntimeError(error)
