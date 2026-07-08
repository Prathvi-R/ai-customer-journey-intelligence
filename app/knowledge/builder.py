from app.models.graph import (
    GraphEdge,
    GraphNode,
    KnowledgeGraph,
)
from app.models.website import WebsiteData


class KnowledgeGraphBuilder:

    @staticmethod
    def build(
        website: WebsiteData,
    ) -> KnowledgeGraph:

        graph = KnowledgeGraph()

        website_node = GraphNode(
            id=website.domain,
            label=website.domain,
            type="website",
        )

        graph.nodes.append(
            website_node
        )

        # ----------------------------------
        # Pages
        # ----------------------------------

        for page in website.pages:

            page_node = GraphNode(
                id=page.url,
                label=page.title,
                type=page.page_type.value,
            )

            graph.nodes.append(
                page_node
            )

            graph.edges.append(
                GraphEdge(
                    source=website.domain,
                    target=page.url,
                    relation="contains",
                )
            )

        # ----------------------------------
        # Projects
        # ----------------------------------

        for project in website.projects.projects:

            project_id = (
                f"project:{project.name}"
            )

            graph.nodes.append(
                GraphNode(
                    id=project_id,
                    label=project.name,
                    type="project",
                )
            )

            graph.edges.append(
                GraphEdge(
                    source=website.domain,
                    target=project_id,
                    relation="offers",
                )
            )

        # ----------------------------------
        # Personas
        # ----------------------------------

        for persona in website.personas.personas:

            persona_id = (
                f"persona:{persona.name}"
            )

            graph.nodes.append(
                GraphNode(
                    id=persona_id,
                    label=persona.name,
                    type="persona",
                )
            )

            graph.edges.append(
                GraphEdge(
                    source=website.domain,
                    target=persona_id,
                    relation="targets",
                )
            )

        return graph