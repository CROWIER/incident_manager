from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from config.database import get_db
from repositories.incident_repository import IncidentRepository
from services.incident_service import IncidentService


def get_incident_repository(db: AsyncSession = Depends(get_db)) -> IncidentRepository:
    return IncidentRepository(db)

def get_incident_service(
    repository: IncidentRepository = Depends(get_incident_repository)
) -> IncidentService:
    return IncidentService(repository)
