from enum import Enum

from pydantic import BaseModel

class CustomerCreateSchema(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Jan",
                "surname": "Kowalski",
                "email": "jan.kowalski@example.com",
                "phone_number": "000-000-000",
            }
        }


class CustomerUpdateSchema(BaseModel):
    name: str | None
    surname: str | None
    email: str | None
    phone_number: str | None

    class Config:
        schema_extra = {
            "example": {
                "name": "Jan",
                "surname": "Kowalski"
            }
        }


class Customer(CustomerCreateSchema):
    id: int

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

class OrderCreateSchema(BaseModel):
    customer_id: int

    class Config:
        schema_extra = {
            "example": {
                "customer_id": 1
            }
        }


class OrderUpdateSchema(BaseModel):
    customer_id: int | None

    class Config:
        schema_extra = {
            "example": {
                "customer_id": 2
            }
        }


class Order(BaseModel):
    id: int
    customer_id: int
    products: list["Product"] = []

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "customer_id": 1,
                "products": [
                    {
                        "id": 1,
                        "name": "Product1",
                        "price": 12.90
                    }
                ]
            }
        }



