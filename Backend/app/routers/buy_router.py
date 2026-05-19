from fastapi import APIRouter
from app.services.buy_service import get_buy_options

router = APIRouter()

@router.get("/buy")
def buy(token: str):
    return get_buy_options(token)