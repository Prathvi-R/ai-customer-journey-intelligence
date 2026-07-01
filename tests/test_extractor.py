import asyncio

from app.services.browser import BrowserService
from app.services.extractor import ExtractionService


async def main():
    browser_service = BrowserService()

    await browser_service.start()

    page = await browser_service.new_page()

    await page.goto(
        "https://shrreejisharan.com",
        wait_until="domcontentloaded",
    )

    page_data = await ExtractionService.extract(page)

    print("=" * 60)
    print("URL         :", page_data.url)
    print("Title       :", page_data.title)
    print("Description :", page_data.description)
    print("Headings    :", len(page_data.headings))
    print("Paragraphs  :", len(page_data.paragraphs))
    print("Buttons     :", len(page_data.buttons))
    print("Forms       :", len(page_data.forms))
    print("Links       :", len(page_data.links))
    print("Images      :", len(page_data.images))
    print("=" * 60)

    await browser_service.close()


if __name__ == "__main__":
    asyncio.run(main())