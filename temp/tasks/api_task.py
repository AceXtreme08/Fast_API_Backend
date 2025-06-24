# get api
# /v1/chaglastore/acdfef/1

from fastapi import FastAPI, Header
from pydantic import AfterValidator, BaseModel
from typing import Annotated


app = FastAPI(title="chagla store🦗")


def get_input(sixaplhabet: str):
    if not (sixaplhabet.isalpha() and len(sixaplhabet) == 6):
        raise ValueError()


Sixalphabet = Annotated[str, AfterValidator(get_input)]


@app.get("/v1/chaglastore/")
def enter(sixalphabet: Sixalphabet):
    return "welcome to chagla store"
