from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.incident import Incident, IncidentStatus


class IncidentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, description: str, source: str) -> Incident:
        incident = Incident(
            description=description,
            source=source
        )
        self.db.add(incident)
        await self.db.commit()
        await self.db.refresh(incident)
        return incident

    async def get_by_id(self, incident_id: int) -> Optional[Incident]:
        result = await self.db.execute(
            select(Incident).where(Incident.id == incident_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self, status: Optional[IncidentStatus] = None) -> list[Incident]:
        query = select(Incident)

        if status:
            query = query.where(Incident.status == status)

        query = query.order_by(Incident.created_at.desc())
        result = await self.db.execute(query)
        return result.scalars().all()

    async def update_status(self, incident_id: int, new_status: IncidentStatus) -> Optional[Incident]:
        incident = await self.get_by_id(incident_id)

        if not incident:
            return None

        incident.status = new_status
        await self.db.commit()
        await self.db.refresh(incident)
        return incident
