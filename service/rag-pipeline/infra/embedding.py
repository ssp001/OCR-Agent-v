from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()
model = HuggingFaceEmbeddings(
    model_name=os.getenv("Embedding_Model")
)
embeddings = model
