from app.models.graph import GraphEdge
from app.models.website import WebsiteData


class RelationshipExtractor:
    """
    Creates semantic relationships
    between extracted entities.
    """

    @staticmethod
    def extract(
        website: WebsiteData,
    ) -> list[GraphEdge]:

        edges: list[GraphEdge] = []

        domain = website.domain

        # -----------------------------
        # Website -> Pages
        # -----------------------------

        for page in website.pages:

            edges.append(
                GraphEdge(
                    source=domain,
                    target=page.url,
                    relation="contains",
                )
            )

        # -----------------------------
        # Website -> Projects
        # -----------------------------

        for project in website.projects.projects:

            edges.append(
                GraphEdge(
                    source=domain,
                    target=f"project:{project.name}",
                    relation="offers",
                )
            )

        # -----------------------------
        # Website -> Personas
        # -----------------------------

        for persona in website.personas.personas:

            edges.append(
                GraphEdge(
                    source=domain,
                    target=f"persona:{persona.name}",
                    relation="targets",
                )
            )

        # -----------------------------
        # Website -> Emails
        # -----------------------------

        for email in website.contacts.emails:

            edges.append(
                GraphEdge(
                    source=domain,
                    target=f"email:{email}",
                    relation="contact",
                )
            )

        # -----------------------------
        # Website -> Phones
        # -----------------------------

        for phone in website.contacts.phone_numbers:

            edges.append(
                GraphEdge(
                    source=domain,
                    target=f"phone:{phone}",
                    relation="contact",
                )
            )

        return edges