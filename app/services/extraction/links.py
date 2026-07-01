from bs4 import BeautifulSoup

from app.services.url import URLService


class LinkExtractor:
    """
    Split links into useful categories.
    """

    @staticmethod
    def extract(
        soup: BeautifulSoup,
        base_url: str,
    ) -> dict:

        internal = []

        external = []

        mailto = []

        telephone = []

        downloads = []

        anchors = []

        for tag in soup.find_all("a", href=True):

            href = tag["href"].strip()

            if href.startswith("#"):
                anchors.append(href)
                continue

            if href.startswith("mailto:"):
                mailto.append(href)
                continue

            if href.startswith("tel:"):
                telephone.append(href)
                continue

            if any(
                href.lower().endswith(ext)
                for ext in (
                    ".pdf",
                    ".doc",
                    ".docx",
                    ".xls",
                    ".xlsx",
                    ".zip",
                )
            ):
                downloads.append(href)
                continue

            absolute = URLService.absolute(base_url, href)

            if URLService.is_internal(base_url, absolute):
                internal.append(absolute)
            else:
                external.append(absolute)

        return {

            "internal_links": sorted(set(internal)),

            "external_links": sorted(set(external)),

            "mailto_links": sorted(set(mailto)),

            "telephone_links": sorted(set(telephone)),

            "download_links": sorted(set(downloads)),

            "anchor_links": sorted(set(anchors)),
        }