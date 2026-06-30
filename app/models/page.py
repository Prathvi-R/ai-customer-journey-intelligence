from pydantic import BaseModel, Field


class PageData(BaseModel):
    # Basic information
    url: str
    title: str = ""
    meta_description: str = ""

    # Content
    headings: list[str] = Field(default_factory=list)
    paragraphs: list[str] = Field(default_factory=list)

    # UI Elements
    buttons: list[str] = Field(default_factory=list)
    forms: list[str] = Field(default_factory=list)

    # Navigation
    internal_links: list[str] = Field(default_factory=list)
    external_links: list[str] = Field(default_factory=list)

    # Media
    images: list[str] = Field(default_factory=list)

    # Metadata
    screenshot_path: str | None = None