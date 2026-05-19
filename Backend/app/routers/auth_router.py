from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.auth_schema import (
    RegisterRequest,
    GenerateOTPRequest,
    VerifyOTPRequest
)

from app.services.auth_service import register_user, delete_user
from app.services.otp_service import generate_otp, verify_user_otp

from app.core.security import get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])

# =========================
# Register
# =========================
@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):

    user = register_user(db, data.username, data.email, data.gender)

    if not user:
        return {"message": "User already exists"}

    return {
        "message": "User registered successfully",
        "user_id": user.id
    }


# =========================
# Generate OTP
# =========================
@router.post("/generate-otp")
def generate_otp_api(data: GenerateOTPRequest, db: Session = Depends(get_db)):

    return generate_otp(db, data.username, data.email)


# =========================
# Verify OTP
# =========================
@router.post("/verify-otp")
def verify_otp_api(data: VerifyOTPRequest, db: Session = Depends(get_db)):

    return verify_user_otp(db, data.username, data.email, data.otp)


# =========================
# Logout
# =========================
@router.post("/logout")
def logout():

    return {"message": "Logged out successfully"}


# =========================
# Delete Account
# =========================
@router.delete("/delete-account")
def delete_account(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    delete_user(db, current_user.id)

    return {"message": "Account deleted"}