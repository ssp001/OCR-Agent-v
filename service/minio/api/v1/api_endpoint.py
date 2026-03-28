"""api endpoints"""

from fastapi import APIRouter
from utils.logger_module import logger
from infra.minio_client import MinioClient
from service.minio_service import MinioService
from dotenv import load_dotenv
import os

# configure module
load_dotenv()
router = APIRouter()
storage_server_client = MinioClient(ip_adress=os.getenv(
    "IP_ADRESS"), access_key=os.getenv("ACCESS_KEY"), secret_key=os.getenv("SECRET_KEY"), security=False)
# === api_routes ===


@router.get("/")
def home():
    return {"message": "this is minio service-endpoint"}


@router.post("/post-endpoint")
def post_endpoint(docs, filename):
    try:
        respones = storage_server_client.post_data(
            docs=docs, filename=filename)
        logger.info("data post operation sucessfull")
        return respones
    except Exception as error:
        logger.error(f"{str(error)}")
        raise RuntimeError(error)
