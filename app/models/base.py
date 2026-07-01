from datetime import datetime
from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    schema_version: str = "1.0.0"

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "extra": "forbid",
    }