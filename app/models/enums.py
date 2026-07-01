from enum import Enum


class CrawlStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class ErrorStage(str, Enum):
    DISCOVERY = "discovery"
    NAVIGATION = "navigation"
    EXTRACTION = "extraction"
    STORAGE = "storage"


class ArtifactType(str, Enum):
    SCREENSHOT = "screenshot"
    HTML = "html"
    PDF = "pdf"


class PageType(str, Enum):
    HOME = "home"
    ABOUT = "about"
    SERVICE = "service"
    PRODUCT = "product"
    BLOG = "blog"
    CONTACT = "contact"
    OTHER = "other"