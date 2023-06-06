from sqlalchemy import Column, ForeignKey, Integer, Float

from config.database import Base

class Supplies(Base):

    __tablename__ = "supplies"

    supplier_id = Column(Integer, ForeignKey("supplier.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    purchase_price = Column(Float)