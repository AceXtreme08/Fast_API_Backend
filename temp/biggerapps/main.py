from fastapi import Depends, FastAPI

import dependencies

import routers.items as rou_it
import routers.users as rou_us


app = FastAPI(dependencies=[Depends(dependencies.get_query_token())])
app.include_router(rou_it.router)
app.include_router(rou_us.router)


@app.get("/")
async def root():
    return {"message": "hello bigger apps"}
