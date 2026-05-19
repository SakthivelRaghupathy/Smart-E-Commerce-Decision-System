import requests
from app.core.config import settings


def get_buy_options(token: str):

    def fetch_stores(page_token):
        url = "https://serpapi.com/search.json"
        params = {
            "engine": "google_immersive_product",
            "page_token": page_token,
            "api_key": settings.SERPAPI_KEY
        }
        res = requests.get(url, params=params)
        data = res.json()

        product_results = data.get("product_results", {})
        return product_results.get("stores", [])


    def extract_token(url):
        if not url or "page_token=" not in url:
            return None
        return url.split("page_token=")[-1].split("&")[0]


    # 🔹 MAIN PRODUCT
    main_stores = fetch_stores(token)

    stores = []

    for item in main_stores:
        price = item.get("extracted_price")
        if not price:
            continue

        stores.append({
            "store_name": clean_store(item.get("name")),
            "price": price,
            "product_link": item.get("link"),
            "delivery": item.get("shipping") or "Standard delivery"
        })

    stores = sorted(stores, key=lambda x: x["price"])

    best = stores[0] if stores else None
    alternatives = stores[1:3]

    # 🔥 SECOND LEVEL FETCH (REAL ALTERNATIVES)
    if len(alternatives) < 2:

        url = "https://serpapi.com/search.json"
        params = {
            "engine": "google_immersive_product",
            "page_token": token,
            "api_key": settings.SERPAPI_KEY
        }

        response = requests.get(url, params=params)
        data = response.json()

        more_options = data.get("product_results", {}).get("more_options", [])

        for opt in more_options:

            new_token = extract_token(opt.get("serpapi_link"))

            if not new_token:
                continue

            alt_stores = fetch_stores(new_token)

            for item in alt_stores:
                price = item.get("extracted_price")
                link = item.get("link")

                if not price or not link:
                    continue

                alternatives.append({
                    "store_name": clean_store(item.get("name")),
                    "price": price,
                    "product_link": link,
                    "delivery": item.get("shipping") or "Standard delivery"
                })

                if len(alternatives) == 2:
                    break

            if len(alternatives) == 2:
                break

    return {
        "best_option": best,
        "alternatives": alternatives
    }


def clean_store(name):
    if not name:
        return "Unknown"
    return name.replace(".in", "").replace(".com", "").strip()