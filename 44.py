from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.post('/files/')
async def create_file(
    filea: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()]
):
    return {
        'filesize': len(filea),
        'token': token,
        'fileb_content_type': fileb.content_type
    }