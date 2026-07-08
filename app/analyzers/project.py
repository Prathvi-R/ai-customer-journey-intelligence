from app.models.page import PageData
from app.models.project import Project, ProjectCatalog
from app.models.enums import PageType


class ProjectAnalyzer:
    """
    Extracts projects, products and services
    from the crawled website.
    """

    @staticmethod
    def analyze(
        pages: list[PageData],
    ) -> ProjectCatalog:

        catalog = ProjectCatalog()

        for page in pages:

            if page.page_type not in (
                PageType.PROJECT,
                PageType.SERVICE,
                PageType.PRODUCT,
            ):
                continue

            description = ""

            if page.paragraphs:
                description = page.paragraphs[0]

            catalog.projects.append(
                Project(
                    name=page.title,
                    url=page.url,
                    description=description,
                    page_type=page.page_type.value,
                    images=page.images[:5],
                )
            )

        return catalog