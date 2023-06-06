from models.supplies import Supplies as SuppliesModel

class SuppliesService():
    def __init__(self,db):
        self.db = db

    def get_for_id(self,id:int):
        result = self.db.query(SuppliesModel).filter(SuppliesModel.supplier_id == id).first()
        return result
    
    def get_for_id(self,id:int):
        result = self.db.query(SuppliesModel).filter(SuppliesModel.product_id == id).first()
        return result

    def create_purchase_price(self,supplies:SuppliesModel):
        new_purchase_price = SuppliesModel(
            purchase_price = supplies.purchase_price.upper()
        )
        self.db.add(new_purchase_price)
        self.db.commit()
        self.db.refresh
        return

    def update_supplier_for_id(self, data:SuppliesModel):
        supplier = self.db.query(SuppliesModel).filter(SuppliesModel.supplier_id == data.supplier_id).first()
        self.db.commit()
        return

    def update_product_for_id(self, data:SuppliesModel):
        product = self.db.query(SuppliesModel).filter(SuppliesModel.product_id == data.product_id).first()
        self.db.commit()
        return

    def delete_supplier_for_id(self,id:int):
        self.db.query(SuppliesModel).filter(SuppliesModel.supplier_id == id).delete()
        self.db.commit()
        return

    def delete_product_for_id(self,id:int):
        self.db.query(SuppliesModel).filter(SuppliesModel.product_id == id).delete()
        self.db.commit()
        return