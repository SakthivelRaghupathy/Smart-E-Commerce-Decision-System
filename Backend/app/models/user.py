from sqlalchemy import Column,String,Integer,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base
class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False) 
    gender = Column(String(20), default="prefer not to say") 
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 
    otp_codes = relationship("OTPCode", back_populates="user", cascade="all, delete")
    saved_products = relationship("SavedProduct",back_populates="user",cascade="all, delete"
)