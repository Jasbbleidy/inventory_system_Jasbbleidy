from fastapi import APIRouter, Path
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from config.database import Session
from models.supplier import Supplier as SuppliertModel 
from service.supplier import SupplierService
from schemas.supplier import Supplier

supplier_router = APIRouter()

@supplier_router.get("/supplier",tags=["supplier"],response_model=List[Supplier],status_code=200)
def get_supplier() -> Supplier:
    db = Session()
    result = SupplierService(db).get_supplier()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@supplier_router.get("/supplier/{id}",tags=["supplier"])
def get_supplier(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = SupplierService(db).get_supplier(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@supplier_router.post("/supplier",tags=["supplier"],status_code=201,response_model=dict)
def create_product(supplier:Supplier)->dict:
    db = Session()
    SupplierService(db).create_supplier(Supplier)
    return JSONResponse(content={"message":"The supplier has been registered","status_code":201})

supplier_router.put("/supplier{id}",tags=["supplier"])
def update_supplier(id:int,supplier:Supplier):
    db =  Session()
    result = SupplierService(db).get_supplier(id)
    if not result:
        return JSONResponse(content={"message":"Record not found","status_code":"404"})
    SupplierService(db).update_supplier(id,supplier)
    return JSONResponse(content={"message":"The supplier has been modified with the id: {id}"})

@supplier_router.delete("/supplier/{id}", tags=["supplier"], response_model=dict, status_code=200)
def delete_supplier(id: int)-> dict:
    db = Session()
    result: SuppliertModel = db.query(SuppliertModel).filter(SuppliertModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Supplier not found"})
    SupplierService(db).delete_product(id)
    return JSONResponse(status_code=200, content={"message": "Supplier has been removed"})