# app/swagger.py

from fastapi.openapi.utils import get_openapi

def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API de Calculadora",
        version="0.1.0",
        description="Esta es una API para realizar operaciones",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
