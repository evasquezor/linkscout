from .checker import check_url
from .parser import extract_links
from .parser import normalize_url

html = """
<html>
    <body>
        <a href="https://google.com">Google</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
    </body>
</html>
"""

def main():
    base_url="https://example.com/blog/"
    href="about"
    status_code = check_url("https://google.com")
    print(f"Google: {status_code}")
    print(extract_links(html))
    print(normalize_url(base_url,href))


if __name__== "__main__":
    main()