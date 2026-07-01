from bs4 import BeautifulSoup


class SEOExtractor:
    """
    Extract SEO-related metadata from a webpage.
    """

    @staticmethod
    def extract(soup: BeautifulSoup) -> dict:

        def meta(name: str) -> str:
            tag = soup.find("meta", attrs={"name": name})
            return tag.get("content", "").strip() if tag else ""

        def property_meta(name: str) -> str:
            tag = soup.find("meta", attrs={"property": name})
            return tag.get("content", "").strip() if tag else ""

        canonical = ""

        canonical_tag = soup.find("link", rel="canonical")

        if canonical_tag:
            canonical = canonical_tag.get("href", "").strip()

        favicon = ""

        favicon_tag = soup.find("link", rel=lambda x: x and "icon" in x.lower())

        if favicon_tag:
            favicon = favicon_tag.get("href", "").strip()

        html = soup.find("html")

        language = html.get("lang", "") if html else ""

        return {

            "description": meta("description"),

            "keywords": meta("keywords"),

            "robots": meta("robots"),

            "canonical": canonical,

            "language": language,

            "favicon": favicon,

            "og_title": property_meta("og:title"),

            "og_description": property_meta("og:description"),

            "og_image": property_meta("og:image"),

            "og_url": property_meta("og:url"),

            "twitter_card": meta("twitter:card"),

            "twitter_title": meta("twitter:title"),

            "twitter_description": meta("twitter:description"),

            "twitter_image": meta("twitter:image"),
        }