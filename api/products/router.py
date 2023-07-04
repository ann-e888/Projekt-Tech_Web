from fastapi import APIRouter, HTTPException
from .storage import get_products_storage
from .schema import ProductCreateSchema, ProductUpdateSchema, Product

router = APIRouter()

PRODUCTS_STORAGE = get_products_storage()

# get_PRODUCTS = [
#     {"id": 1, "product": "Product 1"},
#     {"id": 2, "product": "Product 2"},
#     {"id": 3, "product": "Product 3"},
# ]


@router.get("/")
async def get_products() -> list[Product]:
    return list(get_products_storage().values())

@router.post("/add")
async def create_product(product: ProductCreateSchema) -> Product:
    index = len(get_products_storage()) + 1
    products_storage = get_products_storage()
    products_storage[index] = Product(id=index, **product.dict())
    return products_storage[index]

    
@router.get("/{product_id}")
async def get_product(product_id: int) -> Product:
    try:
        products_storage = get_products_storage()
        return products_storage[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )
    
@router.patch("/update/{product_id}")
async def update_product(
    product_id: int, updated_product: ProductUpdateSchema
) -> Product:
    try:
        PRODUCTS_STORAGE[product_id] = Product(
            **(
                PRODUCTS_STORAGE[product_id].dict()
                | updated_product.dict(exclude_unset=True)
            )
        )
        return PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

@router.delete("/delete/{product_id}")
async def delete_product(product_id: int) -> None:
    try:
        del PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

