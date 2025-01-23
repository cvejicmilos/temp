from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}


# NOT RECOMMENDED: Some HTTP proxies and servers disallow the usage of headers with underscores
@app.get('/wahtever/')
async def read_whatever(strange_header: Annotated[str | None, Header(convert_underscores=False)] = None):
    return {"strange_header": strange_header}

# Multiple headers
@app.get('/asd/')
async def read_asd(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}