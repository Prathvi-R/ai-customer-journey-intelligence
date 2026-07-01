from urllib.parse import urljoin, urlparse, urlunparse, parse_qsl, urlencode


TRACKING_PARAMETERS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "gclid",
}


class URLService:
    """Utility methods for URL normalization and classification."""

    @staticmethod
    def normalize(url: str) -> str:
        parsed = urlparse(url)

        # Remove fragment
        parsed = parsed._replace(fragment="")

        # Remove tracking query params
        query = [
            (k, v)
            for k, v in parse_qsl(parsed.query)
            if k.lower() not in TRACKING_PARAMETERS
        ]

        parsed = parsed._replace(query=urlencode(query))

        normalized = urlunparse(parsed)

        if normalized.endswith("/"):
            normalized = normalized[:-1]

        return normalized

    @staticmethod
    def is_internal(base_url: str, target_url: str) -> bool:
        base = urlparse(base_url)
        target = urlparse(target_url)

        return base.netloc == target.netloc

    @staticmethod
    def absolute(base_url: str, href: str) -> str:
        return urljoin(base_url, href)