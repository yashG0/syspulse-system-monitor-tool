import psutil
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.ws import monitor_socket

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@asynccontextmanager
async def lifespan(app: FastAPI):
    psutil.cpu_percent(interval=None)  # prime cpu counter on startup
    yield


@app.get("/")
async def index():
    return FileResponse("static/index.html")


@app.websocket("/ws/monitor")
async def websocket_endpoint(websocket: WebSocket):
    await monitor_socket(websocket)
