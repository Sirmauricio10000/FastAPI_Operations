from fastapi import APIRouter, HTTPException
from app.controllers import operations_controller
from app.models.schemas import ErrorResponse, OperationsResponse

router = APIRouter()

@router.get("/addition/", response_model=OperationsResponse, responses={400: {"model": ErrorResponse}})
async def sumar_numeros(num1: int, num2: int):
    result = operations_controller.sumar(num1, num2)
    return result

@router.get("/substraction/", response_model=OperationsResponse, responses={400: {"model": ErrorResponse}})
async def restar_numeros(num1: int, num2: int):
    result = operations_controller.restar(num1, num2)
    return result

@router.get("/division/", response_model=OperationsResponse, responses={400: {"model": ErrorResponse}})
async def dividir_numeros(num1: int, num2: int):
    result = operations_controller.dividir(num1, num2)
    return result

@router.get("/multiplication/", response_model=OperationsResponse, responses={400: {"model": ErrorResponse}})
async def multiplicar_numeros(num1: int, num2: int):
    result = operations_controller.multiplicar(num1, num2)
    return result
