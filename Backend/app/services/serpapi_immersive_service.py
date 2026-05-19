import requests
from app.core.config import settings
def get_product_full_details(product_id: str):

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_product",
        "product_id": product_id,
        "api_key": settings.SERPAPI_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data