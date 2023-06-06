from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=35,min_length=3)
    brand: str = Field(max_length=20,min_length=3)
    description: str = Field(max_length=100,min_length=15) 
    price: float = Field(ge=1.50,le=100.00)
    entry_date: int = Field(le=2023)
    availability: int = Field(le=100)
    available_quantity: int = Field(le=1000)

    class Config:
            schema_extra = {
                "example":{
                    "id": 1,
                    "name": "Shampoo",
                    "brand": "Pantene",
                    "description":"Shampoo made with natural products that hydrates and regenerates hair. Use only suitable for dark hair.",
                    "price": 5.98,
                    "entry_date": "02 05 2023",
                    "availability":"88",
                    "available_quantity":"264",
                }
            }
