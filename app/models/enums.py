from enum import Enum


class CrawlStatus(str, Enum):
    SUCCESS = "success"
    PARTIAL = "partial"
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
    PROJECT = "project"
    PRODUCT = "product"
    BLOG = "blog"
    CONTACT = "contact"
    CAREER = "career"
    OTHER = "other"

class SourceType(str, Enum):
    WEBSITE = "website"
    PDF = "pdf"
    INSTAGRAM = "instagram"
    REVIEWS = "reviews"