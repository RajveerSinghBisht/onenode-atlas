from fastapi import FastAPI

from app.api.routes.system import router as system_router

app = FastAPI(
    title="OneNode Atlas API",
    description="Backend API for the OneNode Atlas platform.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.include_router(system_router)
