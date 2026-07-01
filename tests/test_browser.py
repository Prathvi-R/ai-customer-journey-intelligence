import asyncio

from app.services.browser import BrowserService


async def main():
    browser = BrowserService(headless=True)

    await browser.start()

    page = await browser.new_page()

    await page.goto("https://example.com")

    print(await page.title())

    await browser.close()


if __name__ == "__main__":
    asyncio.run(main())