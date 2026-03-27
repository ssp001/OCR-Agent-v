from core.agent_core import AgentCore
from utils.logger_module import logger


class AgentService:
    def __init__(self, client: AgentCore):
        self._agent = client

    def run_as_agent(self, query: str) -> AgentCore:
        try:
            respones = self._agent.genarate(query)
            if respones is TypeError:
                logger.error("the end responed is a typeerror")
            else:
                logger.info("youyr agent is processing the token")
                return respones
        except Exception as e:
            logger.error(e)
            raise RuntimeError(e)
