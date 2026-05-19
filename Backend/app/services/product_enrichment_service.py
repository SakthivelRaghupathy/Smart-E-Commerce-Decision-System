import re
import random

# 🔹 BRAND EXTRACTION
def extract_brand(title: str):
    brands = ["apple", "samsung", "oneplus", "xiaomi", "realme", "dell", "hp", "lenovo"]

    for b in brands:
        if b in title.lower():
            return b.capitalize()

    return title.split()[0] if title else "Unknown"


# 🔹 RAM
def extract_ram(text):
    match = re.search(r'(\d+)\s?gb', text.lower())
    return match.group(1) + "GB" if match else "Unknown"


# 🔹 STORAGE
def extract_storage(text):
    match = re.search(r'(\d+)\s?gb\s?(storage|rom)?', text.lower())
    return match.group(1) + "GB" if match else "Unknown"


# 🔹 FEATURES
def build_features(title):
    ram = extract_ram(title)
    storage = extract_storage(title)
    return f"{ram} RAM, {storage} Storage"


# 🔹 REVIEW COUNT
def generate_review_count(rating):
    if rating >= 4.5:
        return random.randint(5000, 20000)
    elif rating >= 4.0:
        return random.randint(1000, 5000)
    else:
        return random.randint(100, 1000)


# 🔹 SHIPPING
def generate_shipping(price):
    if price and price > 20000:
        return "Free Delivery"
    elif price and price > 10000:
        return "₹99 Delivery"
    else:
        return "₹49 Delivery"


# 🔹 MAIN FUNCTION
def enrich_product(product: dict):

    title = product.get("title", "")
    price = product.get("extracted_price", 0)
    rating = product.get("rating", 3)

    review_count = product.get("reviews") or generate_review_count(rating)

    return {
        "product_id": product.get("product_id"),
        "product_name": title,
        "brand": extract_brand(title),
        "price": price,
        "rating": rating,
        "review_count": review_count,
        "shipping": generate_shipping(price),
        "features": build_features(title),
        "image": product.get("thumbnail"),
        "buy_link": product.get("link"),
        "token": product.get("token")
    }