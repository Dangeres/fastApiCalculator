from pydantic import BaseModel
from typing import Optional


class ExpressionRequest(BaseModel):
    phrase: str


class EvalResponse(BaseModel):
    value: Optional[str] = None
    full_response: str
