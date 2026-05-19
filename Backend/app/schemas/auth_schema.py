from pydantic import BaseModel, EmailStr
from typing import Optional


# -----------------------------
# Register User
# -----------------------------
class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    gender: Optional[str] = "prefer not to say"


class RegisterResponse(BaseModel):
    message: str
    user_id: int


# -----------------------------
# Generate OTP
# -----------------------------
class GenerateOTPRequest(BaseModel):
    username: str
    email: EmailStr


class GenerateOTPResponse(BaseModel):
    message: str
    otp_sent: bool


# -----------------------------
# Verify OTP
# -----------------------------
class VerifyOTPRequest(BaseModel):
    username: str
    email: EmailStr
    otp: str


class VerifyOTPResponse(BaseModel):
    message: str
    access_token: Optional[str] = None
    token_type: Optional[str] = "bearer"


# -----------------------------
# Logout
# -----------------------------
class LogoutResponse(BaseModel):
    message: str


# -----------------------------
# Delete Account
# -----------------------------
class DeleteAccountResponse(BaseModel):
    message: str