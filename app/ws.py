import asyncio
import json

from fastapi import WebSocket, WebSocketDisconnect

from app.metrics import get_all_metrics


async def monitor_socket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            metrics = get_all_metrics()
            await websocket.send_text(json.dumps(metrics))
            await asyncio.sleep(2)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
