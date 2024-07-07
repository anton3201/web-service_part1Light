# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI

# Press the green button in the gutter to run the script.
app: FastAPI = FastAPI()


@app.get("/minus")
def minus(a, b):
    res = int(a) - int(b)
    return res


@app.get("/plus")
def plus(a, b):
    res = int(a) + int(b)
    return res


@app.get("/multiplicat")
def multi(a, b):
    res = int(a) * int(b)
    return res



@app.get("/div")
def div(a, b):
    res = int(a) / int(b)
    return res

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
