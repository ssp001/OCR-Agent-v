from fastapi import APIRouter
from langchain_community.document_loaders import PyPDFLoader
# alll infrastrcher librarry
from infra.vector_store_infra import VectorStoreMethod
from infra.embedding import embeddings
from infra.text_splitter_infra import TextSplitterMethod
from infra.kafka_infra import KafkaClient
from infra.minio_infra import MinioClient
import tempfile
# all service librarry
from service.text_splitter_service import TextSplitterService
from service.vector_store_service import VectorStoreService
from service.minio_service import MinioService
from service.kafka_service import KafkaService
from utils.logger_module import logger
from typing import Any
# Module configuaration
router = APIRouter()
text_splitter_service = TextSplitterService(method=TextSplitterMethod)
minio_service = MinioService(client=MinioClient)
kafka_service = KafkaService(client=KafkaClient)
# api endpoint routes


@router.get("/")
def home():
    return {"message": "Rag pipeline endpoint strutup succesfully"}


@router.post("/store_and_simalrity_search")
async def simalrity_search(query: str, bucket_name: Any | None = None, object_name: Any | None = None):
    try:
        # 1. Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            file_path = tmp.name

        # Minio configuration
        docs = minio_service.get_pdf(bucket_name=bucket_name,
                                     object_name=object_name, file_path=file_path)
        # load the pdf from file path
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        # SPlit the text from pdf
        docs = text_splitter_service.splite_text(docs=documents)
        # store it in vector store
        vector_store = VectorStoreService(
            store=VectorStoreMethod(embedding=embeddings, kwargs=10, docs=[doc.page_content for doc in docs]))
        db_service = VectorStoreService(store=vector_store)
        # respones
        respones = db_service.store_and_search(
            text=docs.page, embedding=embeddings, query=query)
        kafka_service.producer_service(topic="user_data", value=respones)
        logger.info("your data stored in data base succesfully")

        return respones
    except Exception as e:
        logger.error(e)
        raise RuntimeError(e)
