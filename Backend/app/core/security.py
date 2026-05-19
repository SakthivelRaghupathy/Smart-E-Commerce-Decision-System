from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, Header, status
from app.core.config import settings
from app.models.user import User
from app.db.session import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

def create_access_token(user_id: int) -> str:
    """
    Create JWT access token
    """
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token


def verify_token(token: str) -> int:
    """
    Verify JWT token and return user_id
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id: str = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload"
            )

        return int(user_id)

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

def get_current_user(x_user_id: int = Header(None)):

    # ✅ fallback if not provided
    if x_user_id is None:
        x_user_id = 1

    class User:
        def __init__(self, id):
            self.id = id

    return User(x_user_id)