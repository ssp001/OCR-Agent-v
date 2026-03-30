import os
import httpx
from utils.logger_module import logger
from dotenv import load_dotenv
load_dotenv()


async def main(pdf: bytes):
    async with httpx.AsyncClient() as client:
        print("Hello from rag-pipeline!")
        try:
            respones = await client.post(url=os.getenv("RAG_URL"), params={"pdf": pdf})
            if respones.status_code != 200:
                logger.error(
                    f"your pdf can't be uploded ,respones_status:{respones.status_code}respones:{respones.text}")
                return None

            logger.info("your pdf uploded succesfully")
            return {"status": respones.status_code,
                    "respones": respones.text}
        except httpx.RequestError as error:
            logger.error(f"Request faild:{str(error)}")
            return None
