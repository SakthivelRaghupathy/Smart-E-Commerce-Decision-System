from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.base import Base


class SavedProduct(Base):
    __tablename__ = "saved_products"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    product_id = Column(String)

    brand_name = Column(String) 

    product_name = Column(String)

    price = Column(Float)

    rating = Column(Float)

    product_image = Column(String)

    user = relationship("User", back_populates="saved_products")