from pydantic import Field

from app.models.base import BaseData


class PlannerResponse(BaseData):

    agents: list[str] = Field(
        default_factory=list
    )