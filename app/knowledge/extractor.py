from app.models.graph import GraphNode
from app.models.website import WebsiteData


class EntityExtractor:
    """
    Extracts entities from WebsiteData that
    can later be added into the Knowledge Graph.
    """

    @staticmethod
    def extract(
        website: WebsiteData,
    ) -> list[GraphNode]:

        nodes: list[GraphNode] = []

        # -----------------------------
        # Pages
        # -----------------------------

        for page in website.pages:

            nodes.append(
                GraphNode(
                    id=page.url,
                    label=page.title,
                    type=page.page_type.value,
                )
            )

        # -----------------------------
        # Projects
        # -----------------------------

        for project in website.projects.projects:

            nodes.append(
                GraphNode(
                    id=f"project:{project.name}",
                    label=project.name,
                    type="project",
                )
            )

        # -----------------------------
        # Personas
        # -----------------------------

        for persona in website.personas.personas:

            nodes.append(
                GraphNode(
                    id=f"persona:{persona.name}",
                    label=persona.name,
                    type="persona",
                )
            )

        # -----------------------------
        # Contact Emails
        # -----------------------------

        for email in website.contacts.emails:

            nodes.append(
                GraphNode(
                    id=f"email:{email}",
                    label=email,
                    type="email",
                )
            )

        # -----------------------------
        # Phone Numbers
        # -----------------------------

        for phone in website.contacts.phone_numbers:

            nodes.append(
                GraphNode(
                    id=f"phone:{phone}",
                    label=phone,
                    type="phone",
                )
            )

        return nodes