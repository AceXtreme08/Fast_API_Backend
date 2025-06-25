from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header

from .routers.users import router as users_router
from .routers.items import router as items_router


app = FastAPI(dependencies=[Depends(get_query_token())])
app.include_router(users_router)
app.include_router(items_router.router)


@app.get("/")
async def root():
    return {"message": "hello bigger apps"}
