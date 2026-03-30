"""api endpoints"""

from fastapi import APIRouter
from utils.logger_module import logger
from infra.minio_client import MinioClient
from service.minio_service import MinioService
from dotenv import load_dotenv
from infra.kafka_client import KafkaCleint
from service.kafka_service import KafkaService
import os

# configure module
load_dotenv()
router = APIRouter()
storage_server_client = MinioClient(ip_adress=os.getenv(
    "IP_ADRESS"), access_key=os.getenv("ACCESS_KEY"), secret_key=os.getenv("SECRET_KEY"), security=False)
storage_server_service = MinioService(client=storage_server_client)
message_sending_service = KafkaService(client=KafkaCleint)
# === api_routes ===


@router.get("/")
def home():
    return {"message": "this is minio service-endpoint"}


@router.post("/post-endpoint")
def post_endpoint(docs, filename):
    try:
        storage_server_service.post_docs(
            docs=docs, filename=filename)
        logger.info("data post operation sucessfull")
        docs = storage_server_service.get_docs(filename=filename)
        logger.info("file fetched succesfully for kafka sending service")
        message_sending_service.send_message(topic="user_data", value=docs)
        logger.info("kafka message process complete")
    except Exception as error:
        logger.error(f"{str(error)}")
        raise RuntimeError(error)
