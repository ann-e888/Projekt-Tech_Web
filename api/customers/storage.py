from functools import lru_cache

from .schema import Customer, Order

CustomerStorageType = dict[int, Customer]
OrderStorageType = dict[int, list["Order"]]


CUSTOMERS: CustomerStorageType = {}
ORDERS: OrderStorageType = {}


@lru_cache(maxsize=1)
def get_customers_storage() -> CustomerStorageType:
    return CUSTOMERS

@lru_cache(maxsize=1)
def get_orders_storage() -> OrderStorageType:
    return ORDERS

