from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.search_schema import SearchRequest
from app.services.memory_store import init_user, store
from app.core.security import get_current_user
from app.db.session import get_db
from app.services.serpapi_service import search_products_from_serpapi


router = APIRouter()


@router.post("/search")
def search_products(
    data: SearchRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = 2

    # ✅ Initialize user memory
    init_user(user_id)

    # ✅ BUILD SMART QUERY
    query = data.product_name

    if data.brand:
        query = f"{data.brand} {data.product_name}"

    # 🔥 IMPORTANT FIX (better results)
    if data.max_budget:
        query = f"{query} under {data.max_budget}"

    # 🔍 DEBUG (optional)
    # print("FINAL QUERY:", query)

    # ✅ CALL SERPAPI
    serpapi_results = search_products_from_serpapi(
        query,
        data.min_budget,
        data.max_budget
    )

    # ✅ STORE IN MEMORY
    store[user_id]["search_results"] = serpapi_results

    return {"products": serpapi_results}