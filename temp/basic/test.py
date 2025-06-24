# # def get_full_name(first_name: str, last_name: str):
# #     full_name = first_name.title() + " " + last_name.title()
# #     return full_name


# # print(get_full_name("john", "doe"))


# # def get_full_name_with_middle(first_name: str, middle_name: str, last_name: str):
# #     full_name = first_name.title() + " " + middle_name.title() + " " + last_name.title()
# #     return full_name


# # print(get_full_name_with_middle("john", "paul", "doe"))


# # def get_full_name_with_optional_middle(
# #     first_name: str, last_name: str, middle_name: str = ""
# # ):
# #     if middle_name:
# #         full_name = (
# #             first_name.title() + " " + middle_name.title() + " " + last_name.title()
# #         )
# #     else:
# #         full_name = first_name.title() + " " + last_name.title()
# #     return full_name


# # print(get_full_name_with_optional_middle("john", "doe"))
# # print(get_full_name_with_optional_middle("john", "doe", "paul"))


# # def get_name_with_age(name: str, age: int):
# #     name_with_age = name + " is this old: " + str(age)
# #     return name_with_age


# # print(get_name_with_age("john", 35))


# # def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
# #     return item_a, item_b, item_c, item_d, item_d, item_e


# # print(get_items("apple", 10, 3.14, True, b"byte_string"))


# # def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
# #     return items_t, items_s


# # print(process_items((1, 2, "three"), {b"byte1", b"byte2"}))


# # def say_hi(name: str | None = None):
# #     if name is not None:
# #         print(f"Hey {name}!")
# #     else:
# #         print("No Name Provided!")


# # say_hi("John")


# class Person:
#     def __init__(self, name: str):
#         self.name = name


# def get_person_name(one_person: Person):
#     return one_person.name


# print(get_person_name(Person("John Doe")))


# def get_person_name_with_optional(one_person: Person | None = None):
#     if one_person is not None:
#         return one_person.name
#     else:
#         return "No Person Provided!"


# print(get_person_name_with_optional(Person("John Doe")))


# from datetime import datetime

# from pydantic import BaseModel


# class User(BaseModel):
#     id: int
#     name: str = "John Doe"
#     signup_ts: datetime | None = None
#     friends: list[int] = []


# external_data = {
#     "id": "123",
#     "signup_ts": "2017-06-01 12:22",
#     "friends": [1, "2", b"3"],
# }
# user = User(**external_data)
# print(user)
# # > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
# print(user.id)
# # > 123


# # import asyncio
# from fastapi import FastAPI
# import requests

# app = FastAPI()


# @app.get("/")
# async def read_root():
#     response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#     return {"message": "Hello World", "data": response.json()}


from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/users/ace")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users")
async def read_users():
    return ["beeee", "Ceeeeeee"]


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "yes"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "no"}

    return {"model_name": model_name, "message": "neutral"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is a descriptive server response for the item."}
        )
    return item
