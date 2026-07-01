from app.models.enums import PageType
from app.models.page import PageData
from app.services.classification import ClassificationService


pages = [
    PageData(
        url="https://company.com/about",
        domain="company.com",
        title="About Us",
    ),
    PageData(
        url="https://company.com/blogs",
        domain="company.com",
        title="Blogs",
    ),
    PageData(
        url="https://company.com/contact",
        domain="company.com",
        title="Contact",
    ),
]


for page in pages:
    print(
        page.url,
        "->",
        ClassificationService.classify(page),
    )