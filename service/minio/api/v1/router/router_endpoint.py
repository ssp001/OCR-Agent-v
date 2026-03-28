from api.v1 import api_endpoint
from fastapi import FastAPI

app = FastAPI(name="Minio-endpoint",
              description="api endpoint for Minio buckket", version="v1")

app.include_router(router=api_endpoint.router, prefix="/api/v1")
