from typing import Annotated

from fastapi import Form, FastAPI

app = FastAPI()

@app.post('/login/')
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}