from fastapi import APIRouter
from service.agent_service import AgentService
from infra.agent_infrastrucher import HuggingFaceService
from utils.logger_module import logger

router = APIRouter()
llm_provider = HuggingFaceService(verbose=True)
service = AgentService(client=llm_provider)


@router.get("/")
def home_page():
    return {"this is agent endpoint welcome😈"}


@router.post("/endpoint")
async def agent_endpoin(query: str):
    output = await service.run_as_agent(query)
    logger.info("your endpoint is running")
    if output is None:
        logger.error("output is type if null")
        return "output is null"
    else:
        return output
