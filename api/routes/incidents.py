from typing import Optional
from fastapi import APIRouter, Depends, status

from models.incident import IncidentStatus
from api.dependencies import get_incident_service
from services.incident_service import IncidentService
from schemas.incident import IncidentCreate, IncidentUpdate, IncidentResponse, IncidentListResponse

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.post(
    "/",
    response_model=IncidentResponse,
    status_code=status.HTTP_201_CREATED,
    description="Создание нового инцидента"
)
async def create_incident(
        incident_data: IncidentCreate,
        service: IncidentService = Depends(get_incident_service)
) -> IncidentResponse:
    return await service.create_incident(incident_data)


@router.get(
    "/",
    response_model=IncidentListResponse,
    description="Получение списка всех инцидентов"
)
async def get_incidents(
        status: Optional[IncidentStatus] = None,
        service: IncidentService = Depends(get_incident_service)
) -> IncidentListResponse:
    return await service.get_incidents(status)


@router.patch(
    "/{incident_id}",
    response_model=IncidentResponse,
    description="Обновление статуса инцидента по ID"
)
async def update_incident_status(
        incident_id: int,
        update_data: IncidentUpdate,
        service: IncidentService = Depends(get_incident_service)
) -> IncidentResponse:
    return await service.update_incident_status(incident_id, update_data)
