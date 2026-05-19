import requests
from app.core.config import settings


def search_products_from_serpapi(query, min_budget, max_budget):

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_shopping",
        "q": query,
        "hl": "en",
        "gl": "in",
        "api_key": settings.SERPAPI_KEY
    }

    response = requests.get(url, params=params)

    data = response.json()



    products = data.get("shopping_results", [])

    unique_models = {}
    results = []

    for item in products[:20]:  # increase range for better filtering

        title = item.get("title", "")

        # ✅ FIXED PRICE HANDLING
        price = item.get("extracted_price")

        if price is not None:
            if not (min_budget <= price <= max_budget):
                continue
        else:
            price = 0  # allow missing price products

        product = {
            "product_id": item.get("product_id"),
            "model_name": title,
            "brand_name": title.split()[0] if title else "Unknown",
            "price": price,
            "rating": item.get("rating") or 3.5,
            "product_image": item.get("thumbnail"),
            "immersive_product_page_token": item.get(
                "immersive_product_page_token"
            )
        }

        # ✅ REMOVE DUPLICATES
        key = title.lower().split("(")[0].strip()

        if key not in unique_models:
            unique_models[key] = product

    results = list(unique_models.values())[:9]

    return results