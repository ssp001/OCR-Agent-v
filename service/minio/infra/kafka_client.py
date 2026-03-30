from core.kafka_core import KafkaCore
from confluent_kafka import Producer
from typing import Tuple
import json
from utils import logger
from dotenv import load_dotenv
import os
load_dotenv()


class KafkaCleint(KafkaCore):
    def __init__(self):
        config = os.getenv("KAFKA_CONFIG")
        self._p = Producer(config)

    def kafka_producer(self, Topic: str, value: Tuple[str, None, bytes] = None):
        try:
            var = json.dumps(value).encode("utf-8")
            self._p.produce(topic=Topic, value=var)
            self._p.poll(1.0)
            logger.info("kafka_producr task complete succcesfully")
            return None
        except Exception as error:
            raise RuntimeError(error)
