from fastapi import  FastAPI
from fastapi.staticfiles import StaticFiles

# Use this to serve a public/index.html
from starlette.responses import FileResponse 

app = FastAPI()
# app.mount("/public", StaticFiles(directory="app/public"), name="public")
app.mount("/assets", StaticFiles(directory="app/assets"), name="assets")
app.mount("/css", StaticFiles(directory="app/css"), name="css")
app.mount("/js", StaticFiles(directory="app/js"), name="js")

@app.get("/")
async def read_index():
    return FileResponse('app/index.html')

@app.get("/resume")
async def get_resume():
    return FileResponse("app/assets/resumes/ChristopherKok_ResumeMLE.pdf")