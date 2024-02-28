# main.py
from fastapi import FastAPI
from app.routers import operations
from app import swagger
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(operations.router, prefix="/api/v1")

app.openapi = lambda: swagger.custom_openapi(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados en las solicitudes
)
