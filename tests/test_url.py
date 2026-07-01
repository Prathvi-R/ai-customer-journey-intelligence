from app.services.url import URLService


base = "https://shrreejisharan.com"

urls = [
    "/about",
    "https://shrreejisharan.com/contact",
    "https://google.com",
    "https://shrreejisharan.com/?utm_source=test#section",
]

for url in urls:
    absolute = URLService.absolute(base, url)
    normalized = URLService.normalize(absolute)

    print(f"Original   : {url}")
    print(f"Absolute   : {absolute}")
    print(f"Normalized : {normalized}")
    print(f"Internal   : {URLService.is_internal(base, absolute)}")
    print("-" * 50)