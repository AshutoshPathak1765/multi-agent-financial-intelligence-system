from fastapi import APIRouter
from pydantic import BaseModel
from app.services.agent_service import run_agent

router = APIRouter()


class RequestModel(BaseModel):
    input: str


@router.post("/run")
def run(request: RequestModel):
    return run_agent(request.input)
