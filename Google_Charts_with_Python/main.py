from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.routes.renderers.ChartRenderer import chart_renderer
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi_cache.decorator import cache
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(chart_renderer)

@app.get("/home", response_class=HTMLResponse)
async def root(request: Request):
    template = 'Dashboard.html'
    context = {'request': request, 'data': '0'}
    return templates.TemplateResponse(template, context)

def start_server():
    print('Starting Server...')       

    uvicorn.run(
        "app",
        host="localhost",
        port=8000,
        log_level="Debug",
        reload=True
    )

if __name__ == "__main__":
    start_server()

#uvicorn main:app --reload