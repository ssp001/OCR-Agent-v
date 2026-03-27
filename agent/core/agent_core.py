import abc
from typing import List


class AgentCore(abc.ABC):
    @abc.abstractmethod
    def genarate(self) -> List[str]:
        pass
