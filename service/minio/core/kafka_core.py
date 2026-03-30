import abc


class KafkaCore(abc.ABC):
    @abc.abstractmethod
    def kafka_producer(self): ...
