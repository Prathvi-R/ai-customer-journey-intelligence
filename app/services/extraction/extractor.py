from bs4 import BeautifulSoup
from playwright.async_api import Page

from app.models.page import PageData
from app.services.extraction.content import ContentExtractor
from app.services.extraction.links import LinkExtractor
from app.services.extraction.schema import SchemaExtractor
from app.services.extraction.seo import SEOExtractor


class ExtractionService:
    """
    Coordinates all extraction modules and produces
    a fully populated PageData object.
    """

    @staticmethod
    async def extract(page: Page) -> PageData:

        html = await page.content()
        soup = BeautifulSoup(html, "lxml")

        title = ""

        if soup.title and soup.title.string:
            title = soup.title.string.strip()

        seo = SEOExtractor.extract(soup)

        content = ContentExtractor.extract(soup)

        links = LinkExtractor.extract(
            soup,
            page.url,
        )

        schema = SchemaExtractor.extract(soup)

        return PageData(

            # Identity

            url=page.url,
            title=title,
            description=seo["description"],
            language=seo["language"],

            # SEO

            canonical=seo["canonical"],
            keywords=seo["keywords"],
            robots=seo["robots"],
            favicon=seo["favicon"],

            og_title=seo["og_title"],
            og_description=seo["og_description"],
            og_image=seo["og_image"],
            og_url=seo["og_url"],

            twitter_card=seo["twitter_card"],
            twitter_title=seo["twitter_title"],
            twitter_description=seo["twitter_description"],
            twitter_image=seo["twitter_image"],

            # Content

            headings=content["headings"],
            paragraphs=content["paragraphs"],
            buttons=content["buttons"],
            forms=content["forms"],
            images=content["images"],
            lists=content["lists"],
            tables=content["tables"],

            # Links

            internal_links=links["internal_links"],
            external_links=links["external_links"],
            mailto_links=links["mailto_links"],
            telephone_links=links["telephone_links"],
            download_links=links["download_links"],
            anchor_links=links["anchor_links"],

            # Structured Data

            json_ld=schema["json_ld"],
            schema_types=schema["schema_types"],
        )