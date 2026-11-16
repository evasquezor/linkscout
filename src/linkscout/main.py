from .checker import check_url

def main():
    status_code = check_url("https://google.com")
    print(f"Google: {status_code}")


if __name__== "__main__":
    main()