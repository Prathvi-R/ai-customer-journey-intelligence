from pydantic import BaseModel, ConfigDict


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