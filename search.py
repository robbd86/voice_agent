import requests

def search_wikipedia(query):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
    res = requests.get(url).json()
    return {
        "title": res.get("title"),
        "extract": res.get("extract"),
        "url": res.get("content_urls", {}).get("desktop", {}).get("page")
    }