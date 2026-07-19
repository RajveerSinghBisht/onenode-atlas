from pydantic import BaseModel


class ServiceInfoResponse(BaseModel):
    name: str
    version: str


class HealthResponse(BaseModel):
    status: str
