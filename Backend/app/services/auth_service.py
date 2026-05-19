from sqlalchemy.orm import Session
from app.models.user import User


def register_user(db: Session, username: str, email: str, gender: str):

    user = db.query(User).filter(User.email == email).first()

    if user:
        return None

    new_user = User(
        username=username,
        email=email,
        gender=gender
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def delete_user(db: Session, user_id: int):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return False

    db.delete(user)
    db.commit()

    return True