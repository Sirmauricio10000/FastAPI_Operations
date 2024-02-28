from app.models.schemas import OperationsResponse
from fastapi import HTTPException

def sumar(num1: int, num2: int) -> OperationsResponse:
    response = num1 + num2
    return OperationsResponse(result=response)

def restar(num1: int, num2: int) -> OperationsResponse:
    response = num1 - num2
    return OperationsResponse(result=response)

def dividir(num1: int, num2: int) -> OperationsResponse:
    if num2 == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir por cero")
    response = num1 / num2
    return OperationsResponse(result=response)

def multiplicar(num1: int, num2: int) -> OperationsResponse:
    response = num1 * num2
    return OperationsResponse(result=response)
