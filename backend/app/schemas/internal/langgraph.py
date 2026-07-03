from pydantic import BaseModel


class GraphResult(BaseModel):
    response: str
    steps: int
   