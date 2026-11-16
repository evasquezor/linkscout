import httpx

def check_url(url: str) -> int:
    try:
        response = httpx.get(
            url,
            timeout=10,
            follow_redirects=True
        )

        return response.status_code
    
    except httpx.TimeoutException:
        print("Request time out")
    except httpx.ConnectError:
        print("Webist isnt available")