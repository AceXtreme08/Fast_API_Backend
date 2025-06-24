# from fastapi import FastAPI, status, HTTPException
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()


# @app.post("/items/", response_model=Item, status_code=status.HTTP_202_ACCEPTED)
# async def create_item(item: Item):
#     if item.name == "chagla":
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
#     return item


from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Items(BaseModel):
    items: str
    description: str
    price: float
    tax: float
    tag: set[str] = set()


@app.post(
    "/items/",
    response_model=Items,
    summary="Create an Item",
    tags=["Inventory Management"],
    status_code=status.HTTP_207_MULTI_STATUS,
)
async def get_items(item: Items):
    """
    **item** : "name of the item",
    **description** : "desc of item with availability"
    **price** : "item cost"
    **tax** : "item taxation"
    **tag** : "unique ID for identification of item"
    """
    return item
