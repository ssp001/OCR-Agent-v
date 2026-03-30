from core.kafka_core import KafkaCore


class KafkaService:
    def __init__(self, client: KafkaCore):
        self._client = client

    def producer_service(self, topic: str, value: None | str | bytes):
        self._client.producer_service(topic=topic, value=value)
        return "done"
