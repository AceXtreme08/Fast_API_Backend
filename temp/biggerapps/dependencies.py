from fastapi import Header, HTTPException


def get_token_header(x_token: str = Header("fake super secret token")):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X token invalid")


def get_query_token(token: str = "Jessica"):
    if token != "Jessica":
        raise HTTPException(status_code=400, detail="need jessicasss")
