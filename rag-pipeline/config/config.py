from pydantic_settings import BaseSettings


class Base(BaseSettings):
    RAG_URL = "http://127.0.0.1:8000/default/upload_pdf_api_v1_upload_pdf_uplod_pdf_post"
