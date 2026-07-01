from bs4 import BeautifulSoup


class ContentExtractor:
    """
    Extract visible content from HTML.
    """

    @staticmethod
    def extract(soup: BeautifulSoup) -> dict:

        headings = [
            h.get_text(" ", strip=True)
            for h in soup.find_all(
                ["h1", "h2", "h3", "h4", "h5", "h6"]
            )
        ]

        paragraphs = [
            p.get_text(" ", strip=True)
            for p in soup.find_all("p")
            if p.get_text(strip=True)
        ]

        buttons = [
            b.get_text(" ", strip=True)
            for b in soup.find_all("button")
        ]

        forms = [
            f.get("action", "")
            for f in soup.find_all("form")
        ]

        images = [
            img.get("src")
            for img in soup.find_all("img", src=True)
        ]

        lists = []

        for ul in soup.find_all(["ul", "ol"]):

            items = [
                li.get_text(" ", strip=True)
                for li in ul.find_all("li")
            ]

            if items:
                lists.append(items)

        tables = []

        for table in soup.find_all("table"):

            rows = []

            for tr in table.find_all("tr"):

                row = [
                    td.get_text(" ", strip=True)
                    for td in tr.find_all(["td", "th"])
                ]

                if row:
                    rows.append(row)

            if rows:
                tables.append(rows)

        return {

            "headings": headings,

            "paragraphs": paragraphs,

            "buttons": buttons,

            "forms": forms,

            "images": images,

            "lists": lists,

            "tables": tables,
        }