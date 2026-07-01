from app.models.page import PageData


class NavigationAnalyzer:

    @staticmethod
    def extract(
        pages: list[PageData],
    ) -> list[str]:

        nav = []

        for page in pages:

            title = page.title.strip()

            if title and title not in nav:
                nav.append(title)

        return nav