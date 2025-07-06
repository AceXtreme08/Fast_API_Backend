from pydantic import BaseModel, EmailStr
from typing import Dict
from fastapi import HTTPException, status
from utils import hash_password, verify_password, create_access_token
from datetime import timedelta


users_db: Dict[str, dict] = {}

class RegisterRequest(BaseModel):
    email: EmailStr
    full_name: str
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

def register_user(data: RegisterRequest):
    if data.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    users_db[data.username] = {
        "email": data.email,
        "full_name": data.full_name,
        "username": data.username,
        "hashed_password": hash_password(data.password)
    }
    return {"msg": "User registered successfully"}

def authenticate_user(data: LoginRequest):
    user = users_db.get(data.username)
    if not user or not verify_password(data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_access_token(
        data={"sub": data.username},
        expires_delta=timedelta(minutes=30)
    )
    return TokenResponse(access_token=token)
