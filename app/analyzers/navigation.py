from app.models.navigation import NavigationGraph
from app.models.navigation import NavigationNode
from app.models.website import WebsiteData


class NavigationAnalyzer:

    @staticmethod
    def analyze(
        website: WebsiteData,
    ) -> NavigationGraph:

        graph = NavigationGraph()

        page_lookup = {
            page.url: page
            for page in website.pages
        }

        for page in website.pages:

            node = NavigationNode(

                url=page.url,

                title=page.title,

                page_type=page.page_type.value,

                children=[
                    link
                    for link in page.internal_links
                    if link in page_lookup
                ],
            )

            graph.nodes.append(node)

        return graph