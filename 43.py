from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post('/files/')
async def create_file(file: Annotated[bytes | None, File(description="A file read as bytes")] = None):
    if not file:
        return {"message": "no file sent"}
    else:
        return {"file_size": len(file)}
    
@app.post('/uploadfile')
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "no upload file sent"}
    else:
        return {"filename": file.filename}
    
# same thing can be done with lists of bytes or UplocaFiles