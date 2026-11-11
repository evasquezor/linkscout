import httpx

# TO DO : return HTML inhalt
def check_url(url: str):
    headers = {
        "User-Agent": "MyPythonCrawler/1.0",
        "Accept": "text/html"
    }

    try:
        response = httpx.get(
            URL,
            headers=headers,
            timeout=10.0,
            follow_redirects=True
        )

        response.raise_for_status()

        print("Final URL:", response.url)
        print("Status:", response.status_code)
        print("Content-Type:", response.headers.get("content-type"))

        html = response.text

        print(html)
    except httpx.TimeoutException:
        print("The request timed out")

    except httpx.HTTPStatusError as e:
        print("HTTP error:", e.response.status_code)

    except httpx.RequestError as e:
        print("Network error:", e)


def __main__():
    check_url("https://www.google.com")
    