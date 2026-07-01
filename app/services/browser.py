from playwright.async_api import (
    async_playwright,
    Browser,
    BrowserContext,
    Page,
)


class BrowserService:
    """
    BrowserService is the only layer that directly interacts with Playwright.

    Responsibilities:
    - Launch and close the browser
    - Create browser pages
    - Navigate to URLs with crawler-friendly defaults
    - Capture screenshots

    The rest of the application should never call Playwright directly.
    """

    DEFAULT_TIMEOUT = 60000  # milliseconds

    def __init__(self, headless: bool = True):
        self.headless = headless

        self._playwright = None
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None

    async def start(self):
        """
        Launch Playwright and create a reusable browser context.
        """

        self._playwright = await async_playwright().start()

        self.browser = await self._playwright.chromium.launch(
            headless=self.headless,
        )

        self.context = await self.browser.new_context(
            viewport={
                "width": 1440,
                "height": 900,
            },
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/137.0.0.0 Safari/537.36"
            ),
        )

    async def new_page(self) -> Page:
        """
        Create and return a new Playwright page.
        """

        if self.context is None:
            raise RuntimeError(
                "BrowserService has not been started."
            )

        return await self.context.new_page()

    async def goto(
        self,
        page: Page,
        url: str,
        timeout: int | None = None,
        retries: int = 2,
    ) -> None:
        """
        Navigate to a URL using crawler-friendly defaults.

        Parameters
        ----------
        page : Page
            Playwright page instance.

        url : str
            URL to visit.

        timeout : int
            Navigation timeout in milliseconds.

        retries : int
            Number of retry attempts.
        """

        timeout = timeout or self.DEFAULT_TIMEOUT

        last_exception = None

        for attempt in range(retries):
            try:
                await page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=timeout,
                )

                return

            except Exception as exc:
                last_exception = exc

                if attempt == retries - 1:
                    raise last_exception

    async def screenshot(
        self,
        page: Page,
        path: str,
    ) -> None:
        """
        Capture a full-page screenshot.
        """

        await page.screenshot(
            path=path,
            full_page=True,
        )

    async def close(self):
        """
        Close all Playwright resources.
        """

        if self.context:
            await self.context.close()

        if self.browser:
            await self.browser.close()

        if self._playwright:
            await self._playwright.stop()