from pydantic import BaseModel


class ProductCreateSchema(BaseModel):
    name: str
    price: float
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Product1",
                "price": "12.90"
            }
        }



class ProductUpdateSchema(BaseModel):
    name: str | None
    price: float | None

    class Config:
        schema_extra = {
            "example": {
                "name": "Product2",
            }
        }


class Product(ProductCreateSchema):
    id: int