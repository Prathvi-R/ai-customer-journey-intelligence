from playwright.async_api import async_playwright, Browser, BrowserContext, Page


class BrowserService:
    """
    Handles browser lifecycle and page creation.

    This service is intentionally isolated so that the rest of the
    application never depends directly on Playwright.
    """

    def __init__(self, headless: bool = True):
        self.headless = headless

        self._playwright = None
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None

    async def start(self):
        """Launch Playwright and create a browser context."""

        self._playwright = await async_playwright().start()

        self.browser = await self._playwright.chromium.launch(
            headless=self.headless
        )

        self.context = await self.browser.new_context()

    async def new_page(self) -> Page:
        """Create a new browser page."""

        if self.context is None:
            raise RuntimeError("BrowserService has not been started.")

        return await self.context.new_page()

    async def close(self):
        """Close browser resources."""

        if self.context:
            await self.context.close()

        if self.browser:
            await self.browser.close()

        if self._playwright:
            await self._playwright.stop()