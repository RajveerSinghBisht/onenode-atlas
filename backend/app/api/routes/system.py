from fastapi import APIRouter

from app.models.system import HealthResponse, ServiceInfoResponse

router = APIRouter()


@router.get("/", response_model=ServiceInfoResponse)
async def get_service_info() -> ServiceInfoResponse:
    return ServiceInfoResponse(name="OneNode Atlas API", version="0.1.0")


@router.get("/health", response_model=HealthResponse)
async def get_health() -> HealthResponse:
    return HealthResponse(status="ok")
