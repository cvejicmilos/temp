from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

# query not required
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fexedquery")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# query required
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3, max_length=50)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# query required again
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3, max_length=50)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# query required, but can be none
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = ...):
    return {"": "whatever"}