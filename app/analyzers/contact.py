import re

from app.models.contact import ContactData
from app.models.page import PageData


class ContactAnalyzer:
    """
    Extracts contact information from all pages.
    """

    EMAIL_REGEX = re.compile(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    )

    PHONE_REGEX = re.compile(
        r"\+?\d[\d\s\-()]{7,}\d"
    )

    SOCIAL_DOMAINS = (
        "facebook.com",
        "instagram.com",
        "linkedin.com",
        "twitter.com",
        "x.com",
        "youtube.com",
    )

    @staticmethod
    def extract(
        pages: list[PageData],
    ) -> ContactData:

        emails = set()
        phones = set()
        addresses = set()
        social_links = set()

        for page in pages:

            # ----------------------------
            # Search paragraphs
            # ----------------------------

            for paragraph in page.paragraphs:

                emails.update(
                    ContactAnalyzer.EMAIL_REGEX.findall(
                        paragraph
                    )
                )

                phones.update(
                    ContactAnalyzer.PHONE_REGEX.findall(
                        paragraph
                    )
                )

            # ----------------------------
            # Mail links
            # ----------------------------

            for link in page.mailto_links:

                emails.add(
                    link.replace(
                        "mailto:",
                        "",
                    )
                )

            # ----------------------------
            # Telephone links
            # ----------------------------

            for link in page.telephone_links:

                phones.add(
                    link.replace(
                        "tel:",
                        "",
                    )
                )

            # ----------------------------
            # Social links
            # ----------------------------

            for link in page.external_links:

                if any(
                    domain in link
                    for domain in ContactAnalyzer.SOCIAL_DOMAINS
                ):
                    social_links.add(link)

        return ContactData(
            phone_numbers=sorted(phones),
            email_addresses=sorted(emails),
            office_addresses=sorted(addresses),
            social_links=sorted(social_links),
        )