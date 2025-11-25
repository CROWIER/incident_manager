from typing import Optional
from fastapi import HTTPException, status

from models.incident import IncidentStatus
from repositories.incident_repository import IncidentRepository
from schemas.incident import IncidentCreate, IncidentUpdate, IncidentResponse, IncidentListResponse

class IncidentService:
    def __init__(self, repository: IncidentRepository):
        self.repository = repository

    async def create_incident(self, data: IncidentCreate) -> IncidentResponse:
        incident = await self.repository.create(description=data.description, source=data.source)
        return IncidentResponse.model_validate(incident)

    async def get_incidents(self, status: Optional[IncidentStatus] = None) -> IncidentListResponse:
        incidents = await self.repository.get_all(status=status)
        return IncidentListResponse(
            incidents=[IncidentResponse.model_validate(inc) for inc in incidents],
            total=len(incidents)
        )

    async def update_incident_status(self, incident_id: int, data: IncidentUpdate) -> IncidentResponse:
        incident = await self.repository.update_status(incident_id, data.status)
        if not incident:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Инцидент с id {incident_id} не найден"
            )

        return IncidentResponse.model_validate(incident)
