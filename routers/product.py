from fastapi import APIRouter, Path
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from config.database import Session
from models.product import Product as ProductModel
from service.product import ProductService
from schemas.product import Product

product_router = APIRouter()

@product_router.get("/product",tags=["product"],response_model=List[Product],status_code=200)
def get_product() -> Product:
    db = Session()
    result = ProductService(db).get_product()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@product_router.get("/product/{id}",tags=["product"])
def get_product(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = ProductService(db).get_product(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@product_router.post("/product",tags=["product"],status_code=201,response_model=dict)
def create_product(product:Product)->dict:
    db = Session()
    ProductService(db).create_product(Product)
    return JSONResponse(content={"message":"The product has been registered","status_code":201})

@product_router.put("/product{id}",tags=["product"])
def update_product(id:int,product:Product):
    db =  Session()
    result = ProductService(db).get_product(id)
    if not result:
        return JSONResponse(content={"message":"Record not found","status_code":"404"})
    ProductService(db).update_product(id,product)
    return JSONResponse(content={"message":"The product has been modified with the id: {id}"})

@product_router.delete("/product/{id}", tags=["product"], response_model=dict, status_code=200)
def delete_product(id: int)-> dict:
    db = Session()
    result: ProductModel = db.query(ProductModel).filter(ProductModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Product not found"})
    ProductService(db).delete_product(id)
    return JSONResponse(status_code=200, content={"message": "Product has been removed"})