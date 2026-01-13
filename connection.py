import urllib.request


def check(_url, tries=3):
    try:
        for _ in range(tries):
            urllib.request.urlopen(_url).read()
        return True
    except Exception as e:
        pass

    return False


if __name__ == '__main__':
    urls = [
        "https://ice-cream-factory.inso-internal.cognite.ai/docs",
        "https://github.com",
        "https://entra.microsoft.com",
        "https://docs.cdf-bootcamp.cogniteapp.com/",
    ]

    for url in urls:
        r = "is" if check(url) else "is NOT"
        print(f"{url} {r} accessible")