def calculate_scores(price: float, rating: float):

    if rating is None:
        rating = 3

    if price is None or price == 0:
        price = 100000  # fallback

    score = (rating * 20) + (100000 / (price + 1))

    return round(score, 2)