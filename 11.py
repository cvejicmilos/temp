from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = ["asd", "ghj"]):
    query_items = {"q": q}
    return query_items

# list instead of list[str] - note recommended
@app.get("/items/")
async def read_items(q: Annotated[list | None, Query()] = ["asd", "ghj"]):
    query_items = {"q": q}
    return query_items