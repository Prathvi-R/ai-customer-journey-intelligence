from bs4 import BeautifulSoup
from playwright.async_api import Page

from app.models.page import PageData


class ExtractionService:
    """
    Extract structured information from a Playwright page.
    """

    @staticmethod
    async def extract(page: Page) -> PageData:
        html = await page.content()
        soup = BeautifulSoup(html, "lxml")

        title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else ""
        )

        meta = soup.find("meta", attrs={"name": "description"})
        meta_description = (
            meta.get("content", "").strip()
            if meta
            else ""
        )

        headings = [
            h.get_text(" ", strip=True)
            for h in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
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

        links = [
            a.get("href")
            for a in soup.find_all("a", href=True)
        ]

        images = [
            img.get("src")
            for img in soup.find_all("img", src=True)
        ]

        return PageData(
            url=page.url,
            title=title,
            description=meta_description,
            headings=headings,
            paragraphs=paragraphs,
            buttons=buttons,
            forms=forms,
            links=links,
            images=images,
        )