import abc


class VectorStoreCore(abc.ABC):
    @abc.abstractmethod
    def store_and_search(self, query: str):
        pass
