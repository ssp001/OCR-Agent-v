from utils.logger_module import logger
from core.vector_store_core import VectorStoreCore


class VectorStoreService:
    def __init__(self, store: VectorStoreCore):
        self.store = store

    def store_data(self, embedding, text: str):
        try:
            respones = self.store.store_the_chunks(text)
            logger.info("your data is stored sucessfuly")
            return respones
        except Exception as error:
            logger.error(error)
            raise RuntimeError(error)
