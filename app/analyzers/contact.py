import re

from app.models.contact import ContactData
from app.models.page import PageData


EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)

PHONE_PATTERN = re.compile(
    r"(?:\+?\d[\d\s().-]{7,}\d)"
)


class ContactAnalyzer:
    """
    Extract contact information from all crawled pages.
    """

    @staticmethod
    def extract(
        pages: list[PageData],
    ) -> ContactData:

        emails = set()
        phones = set()
        addresses = set()
        socials = set()

        for page in pages:

            text = "\n".join(page.paragraphs)

            emails.update(
                EMAIL_PATTERN.findall(text)
            )

            phones.update(
                PHONE_PATTERN.findall(text)
            )

            for link in page.links:

                lower = link.lower()

                if lower.startswith("mailto:"):
                    emails.add(
                        lower.replace("mailto:", "")
                    )

                elif lower.startswith("tel:"):
                    phones.add(
                        lower.replace("tel:", "")
                    )

                elif any(
                    domain in lower
                    for domain in (
                        "facebook.com",
                        "instagram.com",
                        "linkedin.com",
                        "twitter.com",
                        "x.com",
                        "youtube.com",
                    )
                ):
                    socials.add(link)

        return ContactData(
            phone_numbers=sorted(phones),
            email_addresses=sorted(emails),
            office_addresses=sorted(addresses),
            social_links=sorted(socials),
        )