from utils.logger_module import logger
import httpx
from dotenv import load_dotenv
import os

# module configuration
load_dotenv()


async def main(docs: bytes, filename: str):
    async with httpx.AsyncClient() as client:
        print("Hello from minio!")
        respones = await client.post(url=os.getenv(
            "URL_ENDPOINT"), params={"docs": docs, "filename": filename})
        if respones.status_code != 200:
            logger.error(
                f"respones status code error with status code {respones.status_code}")
            return None
        else:
            logger.info(
                f"respones process sucessful with stus code{respones.status_code}")
            return {"status code": respones.status_code, "respones": respones.json()}


if __name__ == "__main__":
    main()
