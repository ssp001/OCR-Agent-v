from langchain_text_splitters import RecursiveCharacterTextSplitter
from core.text_splitter_core import TextSplliter


class TextSplitterService:
    def __init__(self, method: TextSplliter):
        self._method = method

    def splite_text(self, docs) -> RecursiveCharacterTextSplitter:
        chunks = self._method.split_the_text(docs)
        return chunks
