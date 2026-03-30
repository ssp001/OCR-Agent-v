import abc
from confluent_kafka import Producer


class KafkaCore(abc.ABC):
    @abc.abstractmethod
    def producer_service(topic: str, value: str | None | bytes) -> str: ...
