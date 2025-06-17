from typing import Annotated

from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()


def get_input(sixaplhabet: str):
    if not (sixaplhabet.isalpha() and len(sixaplhabet) == 6):
        raise ValueError()


def input_2(onenumber: int):
    if onenumber > 9 or onenumber < 1:
        raise ValueError("Please enter a number between 1 and 9")


Sixalphabet = Annotated[str, AfterValidator(get_input)]
Onenumber = Annotated[int, AfterValidator(input_2)]


@app.get("/v1/chaglastore/")
async def read_items(product_id: Sixalphabet, product_rating: Onenumber):
    return "welocme to store"
