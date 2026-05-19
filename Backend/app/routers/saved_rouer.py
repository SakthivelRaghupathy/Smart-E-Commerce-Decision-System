from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import get_current_user
from app.schemas.saved_schema import SaveProductRequest
from app.models.saved_product import SavedProduct

router = APIRouter()


@router.post("/save-product")
def save_product(
    data: SaveProductRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    product = SavedProduct(
        user_id=current_user.id,
        product_id=data.product_id,
        brand_name=data.brand_name,
        product_name=data.product_name,
        price=data.price,
        rating=data.rating,
        product_image=data.product_image
    )

    db.add(product)
    db.commit()

    return {"message": "Product saved successfully"}