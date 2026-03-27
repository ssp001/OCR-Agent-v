from fastapi import APIRouter
from fastapi import UploadFile, File
from langchain_community.document_loaders import PyPDFLoader
import tempfile
from core.text_splitter_core import TextSplliter
from core.vector_store_core import VectorStoreCore
from service.text_splitter_service import TextSplitterService
from service.vector_store_service import VectorStoreService
from utils.logger_module import logger
from infra.embedding import embeddings
router = APIRouter()

text_splitter_service = TextSplitterService(method=TextSplliter)
db_service = VectorStoreService(VectorStoreCore)


@router.get("/")
def home():
    return {"message": "Rag pipeline endpoint strutup succesfully"}


@router.post("/uplod-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    global db

    try:    # 1. Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            temp_path = tmp.name
        logger.info("your file fetched succesfully")
    # 2. Load PDF
        loader = PyPDFLoader(temp_path)
        documents = loader.load()
        docs = text_splitter_service.splite_text(docs=documents)
        db_store = db_service.store_data(text=docs, embedding=embeddings)
        logger.info("your data stored in data base succesfully")
        return db_store
    except Exception as e:
        logger.error(e)
        raise RuntimeError(e)
