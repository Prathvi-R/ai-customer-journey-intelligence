import asyncio

from app.services.browser import BrowserService
from app.services.extractor import ExtractionService


async def main():
    browser = BrowserService(headless=True)

    await browser.start()

    page = await browser.new_page()

    await browser.goto(
        page,
        "https://shrreejisharan.com",
    )

    page_data = await ExtractionService.extract(page)

    print("=" * 60)
    print("URL         :", page_data.url)
    print("Title       :", page_data.title)
    print("Description :", page_data.meta_description)
    print("Headings    :", len(page_data.headings))
    print("Paragraphs  :", len(page_data.paragraphs))
    print("Buttons     :", len(page_data.buttons))
    print("Forms       :", len(page_data.forms))
    print("Links       :", len(page_data.links))
    print("Images      :", len(page_data.images))
    print("=" * 60)

    await browser.close()


if __name__ == "__main__":
    asyncio.run(main())