# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    a: float
    b: float


# Press the green button in the gutter to run the script.
app: FastAPI = FastAPI()


@app.post("/minus")
def minus(item: Item):
    res = int(item.a) - int(item.b)
    return res


@app.post("/plus")
def plus(item: Item):
    res = int(item.a) + int(item.b)
    return res


@app.post("/multiplicat")
def multi(item: Item):
    res = int(item.a) * int(item.b)
    return res



@app.post("/div")
def div(item: Item):
    res = int(item.a) / int(item.b)
    return res

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
