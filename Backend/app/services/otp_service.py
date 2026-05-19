import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User
from app.models.otp_codes import OTPCode
from app.core.config import settings


# =========================
# Generate 6-digit OTP
# =========================
def create_otp() -> str:
    return str(random.randint(100000, 999999))


# =========================
# Send OTP Email
# =========================
def send_otp_email(to_email: str, otp: str, username: str):

    body = f"""
Hello {username},

Welcome back to Product AnalytriX 👋

Your OTP for login is: {otp}

This OTP will expire in {settings.OTP_EXPIRY_SECONDS} seconds.

If you did not request this, please ignore this email.

Regards,
Product AnalytriX Team😎
"""

    message = MIMEText(body)
    message["Subject"] = "Your Login OTP"
    message["From"] = settings.SMTP_EMAIL
    message["To"] = to_email

    try:
        server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
        server.starttls()
        server.login(settings.SMTP_EMAIL, settings.SMTP_PASSWORD)
        server.send_message(message)
        server.quit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP email"
        )


# =========================
# Generate & Store OTP
# =========================
def generate_otp(db: Session, username: str, email: str):

    user = db.query(User).filter(
        User.username == username,
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Invalid username or email"
        )

    # Delete old unused OTPs
    db.query(OTPCode).filter(
        OTPCode.user_id == user.id,
        OTPCode.is_used == False
    ).delete()

    db.commit()

    otp = create_otp()

    expires_at = datetime.now(timezone.utc) + timedelta(
        seconds=settings.OTP_EXPIRY_SECONDS
    )

    otp_entry = OTPCode(
        user_id=user.id,
        otp_code=otp,
        expires_at=expires_at,
        is_used=False
    )

    db.add(otp_entry)
    db.commit()

    send_otp_email(user.email, otp, user.username)

    return {"message": "OTP sent successfully"}


# =========================
# Verify OTP
# =========================
def verify_user_otp(db: Session, username: str, email: str, otp: str):

    user = db.query(User).filter(
        User.username == username,
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Invalid username or email"
        )

    otp_entry = db.query(OTPCode).filter(
        OTPCode.user_id == user.id,
        OTPCode.otp_code == otp,
        OTPCode.is_used == False
    ).first()

    if not otp_entry:
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP"
        )

    now = datetime.now(timezone.utc)

    # Check expiration
    if now > otp_entry.expires_at:
        db.delete(otp_entry)
        db.commit()
        raise HTTPException(
            status_code=400,
            detail="OTP expired"
        )

    # Mark OTP as used
    otp_entry.is_used = True
    db.commit()

    return {"message": "Login successful",
            "user_id": user.id
            }