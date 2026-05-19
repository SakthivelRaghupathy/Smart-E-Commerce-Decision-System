from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from app.db.session import get_db
from app.services.memory_store import store
from app.services.scoring_service import calculate_scores
from app.services.serpapi_immersive_service import get_product_full_details
from app.services.product_enrichment_service import enrich_product
from app.core.security import get_current_user
from app.services.memory_store import get_user_store
from sqlalchemy.orm import Session

router = APIRouter()


class AnalyzeRequest(BaseModel):
    product_ids: List[str]


@router.post("/analyze")
def analyze_products(data: AnalyzeRequest, current_user=Depends(get_current_user),db: Session = Depends(get_db)):

    user_id = 2

    user_store = get_user_store(user_id)

    if not user_store["search_results"]:
        return {"error": "No search data found"}

    # ✅ GET SELECTED PRODUCTS
    selected_basic = [
        p for p in user_store["search_results"]
        if str(p["product_id"]) in data.product_ids
    ][:3]

    if not selected_basic:
        return {"error": "No matching products"}

    detailed_products = []

    for p in selected_basic:

        full_data = get_product_full_details(p["product_id"])
        product_info = full_data.get("product_results", {})

        combined = {
            "product_id": p["product_id"],
            "title": product_info.get("title", p.get("model_name")),
            "extracted_price": product_info.get("extracted_price", p.get("price")),
            "rating": product_info.get("rating", p.get("rating")),
            "reviews": product_info.get("reviews"),
            "thumbnail": product_info.get("thumbnail", p.get("product_image")),
            "link": product_info.get("link"),
            "token": p.get("immersive_product_page_token")
        }

        enriched = enrich_product(combined)
        detailed_products.append(enriched)

    # ✅ SCORE
    for p in detailed_products:
        p["deal_score"] = calculate_scores(
            price=p["price"],
            rating=p["rating"]
        )

    # ✅ SORT
    sorted_products = sorted(
        detailed_products,
        key=lambda x: x["deal_score"],
        reverse=True
    )

    # ✅ STORE RESULT
    user_store["analysis_result"] = sorted_products

    return {
        "products": sorted_products
    }


@router.get("/analyze-result")
def get_analysis(current_user=Depends(get_current_user),db: Session = Depends(get_db)):

    user_id = 2
    user_store = get_user_store(user_id)

    return {
        "products": user_store.get("analysis_result", [])
    }