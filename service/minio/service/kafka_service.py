from core.kafka_core import KafkaCore


class KafkaService:
    def __init__(self, client: KafkaCore):
        self._kafka_client = client

    def send_message(self, topic: str, value: bytes | str):
        self._kafka_client.kafka_producer(topic, value)
        return None
