from api import agent_endpoint
from fastapi import FastAPI


app = FastAPI(name="ocr-Agent-v", description="main agent endpoint")


app.include_router(router=agent_endpoint.router,
                   prefix="/api/v1", tags=['endpoint'])
