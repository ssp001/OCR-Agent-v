import abc
from utils.logger_module import logger


class TextSplliter(abc.ABC):
    @abc.abstractmethod
    def split_the_text(self, docs):
        pass
