import abc


class VectorStoreCore(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def store_the_chunks(self):
        pass
