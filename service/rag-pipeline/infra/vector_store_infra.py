from utils.logger_module import logger
from core.vector_store_core import VectorStoreCore
from langchain_community.vectorstores import FAISS


class VectorStoreMethod(VectorStoreCore):
    def __init__(self, chunks, docs):
        self.store = FAISS.from_texts(chunks, docs)

    def store_data(self, text: str):
        try:
            respones = self.store.similarity_search(text)
            logger.info("your data is stored sucessfuly")
            return respones
        except Exception as error:
            logger.error(error)
            raise RuntimeError(error)
