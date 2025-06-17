# funtion to processs age
# def check_age(age: int)
# return:
# age>20 -> not ok
# age<5 -> not ok
# 5<age<20 -> perfect

from typing import Annotated
from pydantic import AfterValidator, BaseModel


def age_handler(age: int):
    if not (5 <= age <= 20):
        raise ValueError("not ok")
    return age


Age = Annotated[int, AfterValidator(age_handler)]


class AgeRequest(BaseModel):
    age: Age


def test_for_students(age: AgeRequest):
    print("logic....")


try:
    test_for_students(AgeRequest({"age": 45}))

    print("ok")
except:
    print("error")
