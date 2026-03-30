import httpx
from typing import *
import os
from utils.logger_module import logger


async def main(db_data: Any):
    print("Hello from agent!")
    async with httpx.AsyncClient() as client:
        respones = await client.post(url=os.getenv("RAG_PIPELINE"), json={"data": db_data})
        if respones.status_code != 200:
            logger.error("rag pipeline data gatherring task error")
        logger.info("data fecthing rag pipeline sucessful")
        return {"respones": respones, "status": respones.status_code}


if __name__ == "__main__":
    main()
