from app.models.enums import PageType
from app.models.page import PageData


class PageClassifier:
    """
    Classifies a webpage into a semantic page type using
    URL, title, headings, buttons and content.
    """

    RULES = {
        PageType.HOME: [
            "/",
            "home",
            "homepage",
        ],
        PageType.ABOUT: [
            "about",
            "about-us",
            "who we are",
            "our story",
            "our company",
            "legacy",
            "vision",
            "mission",
        ],
        PageType.CONTACT: [
            "contact",
            "contact-us",
            "reach us",
            "get in touch",
            "location",
            "office",
            "enquire",
        ],
        PageType.PROJECT: [
            "project",
            "projects",
            "property",
            "properties",
            "development",
            "residential",
            "commercial",
        ],
        PageType.SERVICE: [
            "service",
            "services",
            "solution",
            "solutions",
            "offering",
        ],
        PageType.BLOG: [
            "blog",
            "blogs",
            "article",
            "news",
            "press",
        ],
        PageType.CAREER: [
            "career",
            "careers",
            "job",
            "jobs",
            "join us",
            "hiring",
        ],
        PageType.FAQ: [
            "faq",
            "faqs",
            "questions",
            "help",
            "support",
        ],
        PageType.GALLERY: [
            "gallery",
            "photos",
            "images",
            "media",
        ],
        PageType.LEGAL: [
            "privacy",
            "terms",
            "cookies",
            "disclaimer",
        ],
    }

    WEIGHTS = {
        "url": 10,
        "title": 8,
        "heading": 5,
        "button": 3,
        "paragraph": 1,
    }

    @classmethod
    def classify(cls, page: PageData) -> PageType:

        scores = {
            page_type: 0
            for page_type in PageType
        }

        url = page.url.lower()
        title = page.title.lower()

        headings = [
            h.lower()
            for h in page.headings
        ]

        buttons = [
            b.lower()
            for b in page.buttons
        ]

        paragraphs = [
            p.lower()
            for p in page.paragraphs[:10]
        ]

        # Homepage shortcut
        if url.rstrip("/").count("/") <= 2:
            scores[PageType.HOME] += 25

        for page_type, keywords in cls.RULES.items():

            for keyword in keywords:

                if keyword in url:
                    scores[page_type] += cls.WEIGHTS["url"]

                if keyword in title:
                    scores[page_type] += cls.WEIGHTS["title"]

                for heading in headings:
                    if keyword in heading:
                        scores[page_type] += cls.WEIGHTS["heading"]

                for button in buttons:
                    if keyword in button:
                        scores[page_type] += cls.WEIGHTS["button"]

                for paragraph in paragraphs:
                    if keyword in paragraph:
                        scores[page_type] += cls.WEIGHTS["paragraph"]

        best_type = max(
            scores,
            key=scores.get,
        )

        if scores[best_type] == 0:
            return PageType.OTHER

        return best_type