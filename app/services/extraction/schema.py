import json

from bs4 import BeautifulSoup


class SchemaExtractor:
    """
    Extract JSON-LD structured data.
    """

    @staticmethod
    def extract(soup: BeautifulSoup) -> dict:

        schemas = []

        schema_types = []

        for script in soup.find_all(
            "script",
            attrs={"type": "application/ld+json"},
        ):

            if not script.string:
                continue

            try:

                data = json.loads(script.string)

                schemas.append(data)

                if isinstance(data, dict):

                    schema_type = data.get("@type")

                    if schema_type:
                        schema_types.append(schema_type)

            except Exception:
                pass

        return {

            "json_ld": schemas,

            "schema_types": schema_types,
        }