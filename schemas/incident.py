from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

from models.incident import IncidentStatus, IncidentSource


class IncidentCreate(BaseModel):
    description: str = Field(..., min_length=1, description="Описание инцидента")
    source: IncidentSource = Field(..., description="Источник инцидента")


class IncidentUpdate(BaseModel):
    status: IncidentStatus = Field(..., description="Новый статус инцидента")


class IncidentResponse(BaseModel):
    id: int
    description: str
    status: IncidentStatus
    source: IncidentSource
    created_at: datetime

    class Config:
        from_attributes = True


class IncidentListResponse(BaseModel):
    incidents: list[IncidentResponse]
    total: int
