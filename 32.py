from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    field: str 
    other: str | None = None
    whatever: float | None = None

@app.post('/items/')
async def create_item(item: Item) -> Item:
    return item

@app.get('/items/')
async def read_items() -> list[Item]:
    return [
        Item(field="123"),
        Item(field="dfg")
    ]