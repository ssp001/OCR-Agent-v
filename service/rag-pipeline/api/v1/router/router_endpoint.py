import api.api_endpoint as api_endpoint
from utils.logger_module import logger
from fastapi import FastAPI

app = FastAPI(name="rag pipeline", description="router endpoint")
app.include_router(router=api_endpoint.router, prefix='/api/v1/upload-pdf')
