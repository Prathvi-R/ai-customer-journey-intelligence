from app.models.website import WebsiteData


class PromptFactory:
    """
    Centralized prompt builder for all
    AI intelligence tasks.
    """

    @staticmethod
    def website_context(
        website: WebsiteData,
    ) -> str:

        lines = []

        lines.append(
            f"Website: {website.domain}"
        )

        lines.append("")

        lines.append("Projects:")

        for project in website.projects.projects:
            lines.append(
                f"- {project.name}"
            )

        lines.append("")

        lines.append("Personas:")

        for persona in website.personas.personas:
            lines.append(
                f"- {persona.name}"
            )

        lines.append("")

        lines.append("Pain Points:")

        for pain in website.pain_points.pain_points:
            lines.append(
                f"- {pain.description}"
            )

        lines.append("")

        lines.append("Trust Signals:")

        for signal in website.trust.signals:
            lines.append(
                f"- {signal.category}: {signal.value}"
            )

        return "\n".join(lines)