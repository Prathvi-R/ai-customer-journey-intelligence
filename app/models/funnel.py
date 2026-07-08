from pydantic import Field

from app.models.base import BaseData


class FunnelStage(BaseData):
    """
    Represents one stage of the customer funnel.
    """

    name: str

    pages: list[str] = Field(
        default_factory=list
    )

    conversion_actions: list[str] = Field(
        default_factory=list
    )

    confidence: float = 0.0


class FunnelData(BaseData):
    """
    Represents the complete website funnel.
    """

    awareness: FunnelStage = Field(
        default_factory=lambda: FunnelStage(name="Awareness")
    )

    consideration: FunnelStage = Field(
        default_factory=lambda: FunnelStage(name="Consideration")
    )

    trust: FunnelStage = Field(
        default_factory=lambda: FunnelStage(name="Trust")
    )

    conversion: FunnelStage = Field(
        default_factory=lambda: FunnelStage(name="Conversion")
    )

    retention: FunnelStage = Field(
        default_factory=lambda: FunnelStage(name="Retention")
    )