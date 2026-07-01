from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class BaseData(BaseModel):
    """
    Base model for all application data contracts.

    Every serializable model in the project should inherit from this class.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        populate_by_name=True,
        str_strip_whitespace=True,
    )

    created_at: datetime = Field(default_factory=datetime.utcnow)