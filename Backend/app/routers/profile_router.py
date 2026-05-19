from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from app.models.saved_product import SavedProduct
from app.db.session import get_db
from app.services.profile_service import (
    get_user_profile,
    delete_user_account
)

router = APIRouter()


# ✅ Get Profile + Saved Products
@router.get("/users/profile")
def user_profile(
    x_user_id: int = Header(...),
    db: Session = Depends(get_db)
):
    return get_user_profile(x_user_id, db)


# ✅ Remove Saved Product
@router.delete("/saved-products/{product_id}")
def remove_saved_product(
    product_id: str,
    x_user_id: int = Header(...),
    db: Session = Depends(get_db)
):

    db.query(SavedProduct).filter(
        SavedProduct.user_id == x_user_id,
        SavedProduct.product_id == product_id
    ).delete()

    db.commit()

    return {"message": "Product removed"}


# ✅ Delete Account
@router.delete("/users/delete")
def delete_account(
    x_user_id: int = Header(...),
    db: Session = Depends(get_db)
):
    return delete_user_account(x_user_id, db)


# ✅ Logout (Frontend handles token removal)
@router.post("/logout")
def logout():
    return {"message": "Logged out successfully"}