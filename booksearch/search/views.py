import requests
from django.shortcuts import render

RAKUTEN_API_URL = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
RAKUTEN_APP_ID = "PASTE YOUR RAKUTEN APP ID"

def book_search(request):
    query = request.GET.get("q", "")
    books = []

    if query:
        params = {
            "format": "json",
            "title": query,
            "applicationId": RAKUTEN_APP_ID,
            "hits": 20
        }
        response = requests.get(RAKUTEN_API_URL, params=params)

        if response.status_code == 200:
            books = response.json().get("Items", [])

    return render(request, "search/book_search.html", {"books": books, "query": query})
