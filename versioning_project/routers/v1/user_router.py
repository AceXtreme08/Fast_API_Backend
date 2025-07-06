from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database_assets.database import SessionLocal
from database_assets.models import User as DBUser
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt


SECRET_KEY = "thisismysecretkeyysughdfu9sdf9sfius"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/users/login")



async def get_db():
    async with SessionLocal() as session:
        yield session


class UserCreate(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    username: str
    full_name: str
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str




def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> UserResponse:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        result = await db.execute(select(DBUser).where(DBUser.username == username))
        user = result.scalars().first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return UserResponse(username=user.username, full_name=user.full_name, email=user.email)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")







@router.post("/create", summary="Create User")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DBUser).where(DBUser.username == user.username))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    new_user = DBUser(
        username=user.username,
        full_name=user.full_name,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    await db.commit()
    return {"message": "User created successfully"}





@router.post("/login", response_model=Token, summary="Login and get JWT")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DBUser).where(DBUser.username == form_data.username))
    user = result.scalars().first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse, summary="Get current user")
async def get_me(current_user: UserResponse = Depends(get_current_user)):
    return current_user
