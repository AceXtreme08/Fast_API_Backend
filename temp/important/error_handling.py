# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# items = {"foo": "The Foo Wrestlers",
#          "suxx": "sax sux ki baate",
#          "iron134": "iron player hai tu"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Nhi hai bsdk")
#     return {"item": items[item_id]}
#


# TAKING JASON RESPONSE


# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse


# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name


# app = FastAPI()


# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} is not available."},
#     )


# @app.get("/unicorns/{name}")
# async def read_unicorn(name: str):
#     if name == "yolo" or name == "strife":
#         raise UnicornException(name=name)
#     return {"unicorn_name": name}


# PUTTING CUSTOM response


# from fastapi import FastAPI, HTTPException
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import PlainTextResponse
# from starlette.exceptions import HTTPException as StarletteHTTPException

# app = FastAPI()


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 36:
#         raise HTTPException(status_code=410, detail="baal.")
#     return {"item_id": item_id}


# USING THE REQUEST VALIDATOR BODY


# from fastapi import FastAPI, Request, status
# from fastapi.encoders import jsonable_encoder
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel

# app = FastAPI()


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#     )


# class Item(BaseModel):
#     title: str
#     size: int


# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# Reuse FastAPI's exception handlers


from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"HTTP error!: {repr(exc)}")
    return http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"invalid data!: {exc}")
    return request_validation_exception_handler(request, exc)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}
