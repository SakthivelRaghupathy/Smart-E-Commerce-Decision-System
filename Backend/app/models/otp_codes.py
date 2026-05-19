from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


class OTPCode(Base):
    __tablename__ = "otp_codes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    otp_code = Column(String(6), nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    expires_at = Column(DateTime,nullable=False)
    is_used = Column(Boolean,default=False,nullable=False)
    user = relationship("User", back_populates="otp_codes")