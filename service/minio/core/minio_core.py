import abc


class MinioCore(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_data() -> bytes: ...
    @abc.abstractmethod
    def post_data() -> bytes: ...
