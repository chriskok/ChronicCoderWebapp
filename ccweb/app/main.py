from fastapi import  FastAPI
from fastapi.staticfiles import StaticFiles

# Use this to serve a public/index.html
from starlette.responses import FileResponse 

app = FastAPI()
app.mount("/public", StaticFiles(directory="app/public"), name="public")

@app.get("/")
async def read_index():
    return FileResponse('app/public/index.html')