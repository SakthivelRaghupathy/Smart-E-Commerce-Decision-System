from sqlalchemy.orm import Session
from app.models.saved_product import SavedProduct
from app.models.user import User


def get_user_profile(user_id: int, db: Session):

    user = db.query(User).filter(User.id == user_id).first()

    saved_products = db.query(SavedProduct).filter(
        SavedProduct.user_id == user_id
    ).all()

    products = []

    for p in saved_products:
        products.append({
            "product_id": p.product_id,
            "product_name": p.product_name,
            "price": p.price,
            "rating": p.rating,
            "product_image": p.product_image
        })

    return {
        "username": user.username,
        "email": user.email,
        "saved_products": products
    }


def delete_user_account(user_id: int, db: Session):

    db.query(SavedProduct).filter(
        SavedProduct.user_id == user_id
    ).delete()

    db.query(User).filter(User.id == user_id).delete()

    db.commit()

    return {"message": "Account deleted successfully"}