from config.configure import USERCLASS
from core.agent_core import AgentCore
from langchain_huggingface.chat_models import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from langchain.agents import create_agent
from utils.logger_module import logger
from typing import List
import os
from dotenv import load_dotenv
load_dotenv()


class HuggingFaceService(AgentCore):

    def __init__(self, verbose: bool):
        self._verbose: bool = verbose
        self._llm = HuggingFaceEndpoint(
            huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"), model=USERCLASS.LLM, verbose=self._verbose, temperature=0.1)
        self._prompt = """You are an intelligent AI assistant.

                    Your goal is to help users by understanding their questions and providing clear, accurate, and helpful answers.

                    Guidelines:
                    1. Understand the user's request carefully.
                    2. If the request is unclear, ask follow-up questions.
                    3. Provide step-by-step explanations when solving problems.
                    4. Be concise but informative.
                    5. If you do not know the answer, say you are not sure instead of making up information.
                    6. Always respond in a polite and professional tone.

                    User Question:
                    {input}

                    Answer:"""
        self._model = ChatHuggingFace(llm=self._llm)
        self._agent = create_agent(
            model=self._model, system_prompt=self._prompt)

    async def genarate(self, query: dict) -> List[str]:
        try:
            result = []
            async for chanks in self._agent.astream({"input": query}):
                logger.info("your agent is running and processing the tokens")
                logger.info(f"TYPE: {type(chanks)}, VALUE: {chanks}")
                result.append(chanks["model"]["messages"][0].content)
            return {"output": result}
        except Exception as error:
            logger.error(f"there is a error {error}")
            raise TypeError(error)
