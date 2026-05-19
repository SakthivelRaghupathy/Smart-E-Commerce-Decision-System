from pydantic import BaseModel
from typing import List


class AnalyzeRequest(BaseModel):
    products: List[str]   # product ids


class AnalyzeResponse(BaseModel):
    product_id: str
    brand_name: str
    product_name: str
    features: str
    price: float
    rating: float
    link: str
    deal_score: float
    token: str