from pydantic import BaseModel, Field
from typing import Optional

class Supplier(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=35,min_length=3)
    address: str = Field(max_length=50,min_length=15)
    phone: int = Field
    email: str = Field(max_length=30,min_length=10)

    class Config:
            schema_extra = {
                "example":{
                    "id": 3208,
                    "name": "Michael Harris",
                    "address": "Mrs Smith 813 Howard Street Oswego NY 13126 USA",
                    "phone":52764429,
                    "email":"harris.ml@hotmail.com",
                }
            }