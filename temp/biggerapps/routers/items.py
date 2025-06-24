from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"desc not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/item_id")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.get(
    "/{items_id}", tags=["custom"], responses={403: {"descrption": "Op forbidden"}}
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(status_code=409, detail="conflict---update plumbus only")
    return {"item_id": item_id, "name": "great plumbus"}
