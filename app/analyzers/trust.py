import re

from app.models.page import PageData
from app.models.trust import TrustData, TrustSignal


class TrustAnalyzer:
    """
    Extracts trust signals across the website.

    Examples:
    - 30+ Years
    - 2000+ Families
    - ISO Certified
    - Awards
    - Testimonials
    """

    YEAR_PATTERN = re.compile(
        r"(\d+)\s*\+?\s*(?:years?|yrs?)",
        re.IGNORECASE,
    )

    PROJECT_PATTERN = re.compile(
        r"(\d+)\s*\+?\s*projects?",
        re.IGNORECASE,
    )

    CUSTOMER_PATTERN = re.compile(
        r"(\d+)\s*\+?\s*(?:clients?|customers?|families?)",
        re.IGNORECASE,
    )

    AWARD_KEYWORDS = (
        "award",
        "winner",
        "recognition",
        "honour",
        "honor",
        "achievement",
    )

    CERTIFICATION_KEYWORDS = (
        "iso",
        "certified",
        "certificate",
        "certification",
        "rera",
    )

    @staticmethod
    def analyze(
        pages: list[PageData],
    ) -> TrustData:

        trust = TrustData()

        for page in pages:

            content = "\n".join(
                page.headings + page.paragraphs
            )

            # -----------------------------
            # Experience
            # -----------------------------

            years = TrustAnalyzer.YEAR_PATTERN.findall(
                content
            )

            for year in years:

                value = int(year)

                if (
                    trust.experience_years is None
                    or value > trust.experience_years
                ):
                    trust.experience_years = value

                trust.signals.append(
                    TrustSignal(
                        category="experience",
                        value=f"{value} years",
                        page=page.url,
                    )
                )

            # -----------------------------
            # Projects
            # -----------------------------

            projects = TrustAnalyzer.PROJECT_PATTERN.findall(
                content
            )

            for project in projects:

                value = int(project)

                if (
                    trust.projects_completed is None
                    or value > trust.projects_completed
                ):
                    trust.projects_completed = value

                trust.signals.append(
                    TrustSignal(
                        category="projects",
                        value=str(value),
                        page=page.url,
                    )
                )

            # -----------------------------
            # Customers / Families
            # -----------------------------

            customers = TrustAnalyzer.CUSTOMER_PATTERN.findall(
                content
            )

            for customer in customers:

                value = int(customer)

                if (
                    trust.customers is None
                    or value > trust.customers
                ):
                    trust.customers = value

                trust.signals.append(
                    TrustSignal(
                        category="customers",
                        value=str(value),
                        page=page.url,
                    )
                )

            # -----------------------------
            # Awards
            # -----------------------------

            for paragraph in page.paragraphs:

                lower = paragraph.lower()

                if any(
                    keyword in lower
                    for keyword in TrustAnalyzer.AWARD_KEYWORDS
                ):

                    trust.awards.append(paragraph)

                    trust.signals.append(
                        TrustSignal(
                            category="award",
                            value=paragraph,
                            page=page.url,
                        )
                    )

            # -----------------------------
            # Certifications
            # -----------------------------

            for paragraph in page.paragraphs:

                lower = paragraph.lower()

                if any(
                    keyword in lower
                    for keyword in TrustAnalyzer.CERTIFICATION_KEYWORDS
                ):

                    trust.certifications.append(paragraph)

                    trust.signals.append(
                        TrustSignal(
                            category="certification",
                            value=paragraph,
                            page=page.url,
                        )
                    )

        trust.awards = sorted(set(trust.awards))

        trust.certifications = sorted(
            set(trust.certifications)
        )

        return trust