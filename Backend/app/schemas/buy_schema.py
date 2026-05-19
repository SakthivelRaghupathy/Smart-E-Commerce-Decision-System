from pydantic import BaseModel
from typing import List, Optional


class StoreOption(BaseModel):
    store_name: str
    price: float
    product_link: Optional[str]
    delivery: Optional[str]


class BuyResponse(BaseModel):
    best_option: Optional[StoreOption]
    alternatives: List[StoreOption]