from app.models.page import PageData
from app.models.enums import PageType


class ProjectsAnalyzer:

    @staticmethod
    def extract(
        pages: list[PageData],
    ) -> list[str]:

        projects = []

        for page in pages:

            if page.page_type == PageType.PROJECT:
                projects.append(page.title)

        return projects