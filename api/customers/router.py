from fastapi import APIRouter, HTTPException, Query

from .storage import get_customers_storage, get_orders_storage
from .schema import CustomerCreateSchema, CustomerUpdateSchema, Customer
from .schema import OrderCreateSchema, OrderUpdateSchema, Order
from .schema import ProductCreateSchema, ProductUpdateSchema, Product

import os
import sys

current = os.path.dirname(os.path.abspath(__file__))
added = os.path.join(current, '..', 'products')
sys.path.append(added)

from products import storage, schema


router = APIRouter()

ORDERS_STORAGE = get_orders_storage()
CUSTOMERS_STORAGE = get_customers_storage()
PRODUCTS_STORAGE = storage.get_products_storage()


@router.get("/")
async def get_customers() -> list[Customer]:
    return list(get_customers_storage().values())

@router.get("/get-orders")
async def get_orders():
    return ORDERS_STORAGE


@router.get("/{customer_id}")
async def get_customer(customer_id: int) -> Customer:
    try:
        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )


@router.patch("/update-customer/{customer_id}")
async def update_customer(
    customer_id: int, updated_customer: CustomerUpdateSchema
) -> Customer:
    try:
        CUSTOMERS_STORAGE[customer_id] = Customer(
            **(
                CUSTOMERS_STORAGE[customer_id].dict()
                | updated_customer.dict(exclude_unset=True)
            )
        )
        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )


@router.delete("/delete/{customer_id}")
async def delete_customer(customer_id: int) -> None:
    try:
        del CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )


@router.post("/")
async def create_customer(customer: CustomerCreateSchema) -> Customer:
    index = len(CUSTOMERS_STORAGE)
    CUSTOMERS_STORAGE[index] = Customer(id=index, **customer.dict())

    return CUSTOMERS_STORAGE[index]


@router.post("/{customer_id}/add-order")
async def create_order(customer_id: int, order: OrderCreateSchema):
    order_id = len(ORDERS_STORAGE) + 1
    order_data = {
        "id": order_id,
        "customer_id": customer_id,
        "products": []
    }
    ORDERS_STORAGE.setdefault(customer_id, []).append(order_data)

    return order_data

@router.patch("/{customer_id}/orders/{order_id}/add-product")
async def add_product_to_order(customer_id: int, order_id: int, product: ProductCreateSchema):
    order_list = ORDERS_STORAGE.get(customer_id, [])
    for order in order_list:
        if order["id"] == order_id:
            product_id = len(order["products"]) + 1
            product_data = {
                "id": product_id,
                "name": product.name,
                "price": product.price
            }
            order["products"].append(product_data)
            return product_data

    raise HTTPException(
        status_code=404, detail=f"Order with ID={order_id} does not exist for Customer with ID={customer_id}."
    )

@router.delete("/{customer_id}/orders/{order_id}")
async def delete_order(customer_id: int, order_id: int) -> None:
    order_list = ORDERS_STORAGE.get(customer_id, [])
    for order in order_list:
        if order["id"] == order_id:
            order_list.remove(order)
            return

    raise HTTPException(
        status_code=404, detail=f"Order with ID={order_id} does not exist for Customer with ID={customer_id}."
    )


