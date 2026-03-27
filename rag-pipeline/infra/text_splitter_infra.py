from utils.logger_module import logger
from langchain_text_splitters import RecursiveCharacterTextSplitter
from core.text_splitter_core import TextSplliter
from typing import List


class TextSplitterMethod(TextSplliter):
    def __init__(self, method: TextSplliter):
        self._metod = method

    def split_the_text(self, docs: List[str]) -> RecursiveCharacterTextSplitter:
        try:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500, chunk_overlap=50)
            chunks = splitter.split_documents(docs)
            logger.info("your pdf are fetched sussesflley")
            return chunks
        except Exception as error:
            logger.error(error)
            raise RuntimeError(error)
