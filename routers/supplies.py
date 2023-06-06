from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from models.supplies import Supplies as SuppliesModel
from schemas.supplies import Supplies 
from service.supplies import SuppliesService


supplies_router = APIRouter()


@supplies_router.get("/supplier_for_id", tags=["supplier","purchase_price"],status_code=200)
def get_supplier_for_id(id:int):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@supplies_router.get("/product_for_id", tags=["product","purchase_price"],status_code=200)
def get_product_for_id(id:int):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@supplies_router.post("/purchase_price", tags=["purchase_price"], status_code=201)
def create_purchase_price(purchase_price:Supplies):
    db = Session()
    SuppliesService(db).create_purchase_price(purchase_price)
    return JSONResponse(content={"message":"purchase price created sucessfull","status_code":201})

@supplies_router.put("/actors{id}", tags=["supplier","purchase_price"])
def update_supplier_for_id(id:int, supplier_id:Supplies):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message": "supplies don´t gound","status_code":404})
    SuppliesService(db).update_supplier_for_id(Supplies)
    return JSONResponse(content={"message":"suppler update successfully", "status_code":202}, status_code=200)

@supplies_router.put("/product{id}", tags=["product","purchase_price"])
def update_product_for_id(id:int, product_id:Supplies):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"product don´t gound","status_code":404})
    SuppliesService(db).update_product_for_id(Supplies)
    return JSONResponse(content={'message':'movies update successfully', 'status_code':202}, status_code=200)

@supplies_router.delete("/actor{id}",tags=["supplier","purchase_price"])
def delete_supplier_for_id(id:int):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"supplier don´t gound", "status_code":404})
    SuppliesService(db).delete_supplier_for_id(id)
    return JSONResponse(content={"message":"supplier delete sucessfully","status_code":200}, status_code=200)

@supplies_router.delete("/movies{id}",tags=["product","purchase_price"])
def delete_product_for_id(id:int):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"movies don´t gound", "status_code":404})
    SuppliesService(db).delete_product_for_id(id)
    return JSONResponse(content={"message":"movies delete sucessfully","status_code":200}, status_code=200)