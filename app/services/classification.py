from app.models.enums import PageType
from app.models.page import PageData


class ClassificationService:
    """
    Determines the functional purpose of a page.

    Uses URL, title and headings.
    """

    @staticmethod
    def classify(page: PageData) -> PageType:

        url = page.url.lower()

        title = page.title.lower()

        headings = " ".join(page.headings).lower()

        text = f"{url} {title} {headings}"

        if url.endswith("/"):
            return PageType.HOME

        if "about" in text:
            return PageType.ABOUT

        if "contact" in text:
            return PageType.CONTACT

        if "career" in text:
            return PageType.CAREER

        if "blog" in text:
            return PageType.BLOG

        if any(
            word in text
            for word in [
                "project",
                "portfolio",
                "completed project",
                "ongoing project",
            ]
        ):
            return PageType.PROJECT

        if any(
            word in text
            for word in [
                "service",
                "solution",
                "what we do",
            ]
        ):
            return PageType.SERVICE

        if any(
            word in text
            for word in [
                "product",
                "pricing",
                "buy",
                "shop",
            ]
        ):
            return PageType.PRODUCT

        return PageType.OTHER