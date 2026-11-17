from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag

def extract_links(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")

    links_group = []

    for link in links:
        link_href = link.get("href")
        if is_valid_link(link_href):
            links_group.append(link_href)
    return links_group

def normalize_url(base_url: str, href: str) -> str:
    result = urljoin(base_url, href)
    result,_ = urldefrag(result)
    return result

def is_valid_link(href: str) -> bool:
    if not href:
        return False

    href = href.strip().lower()

    ignored_prefixes = (
        "malito:",
        "tel:",
        "javascript:"
    ) 

    if href.startswith(ignored_prefixes):
        return False

    if href.startswith("#"):
        return False

    return True