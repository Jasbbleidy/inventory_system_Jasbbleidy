from pydantic import BaseModel, Field
from typing import Optional

class Supplies(BaseModel):
    supplier_id : int = Field(ge=1, description="supplier id")
    product_id : int = Field(ge=1, description="product id")
    purchase_price: float = Field(ge=90.00,le=500.00)

    class Config:
            schema_extra = {
                "example":{
                    "supplier id": 25,
                    "product id": 3619,
                    "purchase price": 205.40,
                }
            }