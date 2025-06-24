from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, AfterValidator
from typing import Annotated


app = FastAPI()


class Userresponse(BaseModel):
    user_name: str
    user_email: EmailStr


def valid_password(password):
    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
    return has_letter and has_number


def get_password_input(password: str):
    if len(password) < 8 or not valid_password(password):
        raise ValueError("bad password dear")


password = Annotated[str, AfterValidator(get_password_input)]
username = Annotated[str, "username"]
email = Annotated[EmailStr, "email"]


@app.get("/make_a_new_user/")
async def create_user(username: username, password: password, email: email):
    return Userresponse(user_name=username, user_email=email)

