from pydantic import BaseModel
from typing import Optional


class SearchRequest(BaseModel):
    category: str
    product_name: str
    brand: Optional[str] = None
    min_budget: float
    max_budget: float

class ProductResult(BaseModel):
    product_id: str
    brand_name: str
    product_name: str
    price: float
    rating: Optional[float] = None
    product_image: Optional[str] = None