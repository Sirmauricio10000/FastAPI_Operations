from pydantic import BaseModel

class OperationsResponse(BaseModel):
    result: float

class ErrorResponse(BaseModel):
    detail: str
