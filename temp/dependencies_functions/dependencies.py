# from typing import Annotated
# from fastapi import Depends, FastAPI, status

# app = FastAPI()


# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}


# CommonsDep = Annotated[dict, Depends(common_parameters)]

# @app.get("/items/", status_code=status.HTTP_201_CREATED)
# async def read_items(commons: CommonsDep):
#     return commons


# @app.get("/users/", status_code=status.HTTP_202_ACCEPTED)
# async def read_users(commons: CommonsDep):
#     return commons




#sub - dependencies



# from typing import Annotated

# from fastapi import Cookie, Depends, FastAPI

# app = FastAPI()


# def query_extractor(q: str | None = None):
#     return q


# def query_or_cookie_extractor(
#     q: Annotated[str, Depends(query_extractor)],
#     last_query: Annotated[str | None, Cookie()] = None,
# ):
#     if not q:
#         return last_query
#     return q


# @app.get("/items/")
# async def read_query(
#     query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
# ):
#     return {"q_or_cookie": query_or_default}




# dependencies in path operation decorators


# from typing import Annotated
# from pydantic import BaseModel

# from fastapi import Depends, FastAPI, Header, HTTPException, status

# app = FastAPI()


# async def verify_token(x_token: Annotated[str, Header()]):
#     if x_token != "xxxx":
#         raise HTTPException(status_code=400, detail="X-Token header invalid")


# async def verify_key(x_key: Annotated[str, Header()]):
#     if x_key != "yyyy":
#         raise HTTPException(status_code=400, detail="X-Key header invalid")
#     return x_key


# @app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)],status_code=status.HTTP_100_CONTINUE )
# async def read_items():
#     return [{"item": "Foo"}, {"item": "Bar"}]



from fastapi import Depends, FastAPI, Header, HTTPException
from typing_extensions import Annotated


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "xxxx":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "yyyy":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]