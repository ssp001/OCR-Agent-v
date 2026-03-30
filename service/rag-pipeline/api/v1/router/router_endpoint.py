from fastapi import FastAPI
from api import api_endpoint

app = FastAPI(name="rag pipeline", description="router endpoint")
app.include_router(router=api_endpoint.router,
                   prefix='/api/v1/store_and_simalrity_search')
