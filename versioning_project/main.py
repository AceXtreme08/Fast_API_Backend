from fastapi import FastAPI
from routers.v1.health_router import router as h_r
from routers.v1.user_router import router as h_u
from database_assets.database import engine, Base


app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(h_r, prefix="/v1")
app.include_router(h_u, prefix="/v1")
