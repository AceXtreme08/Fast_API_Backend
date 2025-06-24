from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel, EmailStr, AfterValidator

app = FastAPI(title="Form Data Example",
             description="An example of using FormData with FastAPI",
             version="1.0.0")


def valid_password(password: str):
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
        raise ValueError("error pass")




class FormData(BaseModel):
    user_name: str
    e_mail : EmailStr
    password : Annotated[str, AfterValidator(get_password_input)]



@app.post("/login/")
async def login( data: Annotated[FormData, Form()]):
    return data