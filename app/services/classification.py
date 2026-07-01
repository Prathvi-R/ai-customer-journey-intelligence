from app.models.enums import PageType
from app.models.page import PageData


class ClassificationService:
    """
    Deterministic page classifier.

    Uses URL and title heuristics to classify pages.
    No AI is involved at this stage.
    """

    @staticmethod
    def classify(page: PageData) -> PageType:

        url = page.url.lower()
        title = page.title.lower()

        text = f"{url} {title}"

        if (
            url.rstrip("/") == f"https://{page.url.split('/')[2]}"
            or url.count("/") <= 2
        ):
            return PageType.HOME

        if "about" in text:
            return PageType.ABOUT

        if "project" in text:
            return PageType.PROJECT

        if "product" in text:
            return PageType.PRODUCT

        if "blog" in text:
            return PageType.BLOG

        if "career" in text or "job" in text:
            return PageType.CAREER

        if "contact" in text:
            return PageType.CONTACT

        if "service" in text:
            return PageType.SERVICE

        return PageType.OTHER