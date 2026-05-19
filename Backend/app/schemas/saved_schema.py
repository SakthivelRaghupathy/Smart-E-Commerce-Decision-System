from pydantic import BaseModel
from typing import Optional


class SaveProductRequest(BaseModel):
    product_id: str
    brand_name: str
    product_name: str
    price: float
    rating: Optional[float] = None
    product_image: Optional[str] = None