from confluent_kafka import Producer
from core.kafka_core import KafkaCore
from utils.logger_module import logger
import json
import os
from dotenv import load_dotenv
load_dotenv()


class KafkaClient(KafkaCore):
    def __init__(self):
        config = os.getenv("KAFKA_CONFIG")
        self._pod = Producer(config)

    def producer_service(self, topic: str, data: str | bytes | None):
        try:
            var = json.dumps(data).encode("utf-8")
            self._pod.produce(topic=topic, value=var)
            self._pod.poll(1.0)
            logger.info("producer service task compleate")
        except Exception as error:
            logger.error(f"{error}")
            raise RuntimeError(error)
