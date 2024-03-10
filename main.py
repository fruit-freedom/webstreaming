import asyncio
import os

import fastapi
from fastapi import WebSocket
from fastapi.responses import FileResponse, Response

app = fastapi.FastAPI()



@app.get('/')
async def index():
    return FileResponse('index.html')

@app.get('/{filepath:path}')
async def index(filepath: str):
    if not os.path.exists(filepath):
        return Response(status_code=404)
    return FileResponse(f'{filepath}')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    timestamp = 0
    while True:
        # data = await websocket.receive_json()
        await websocket.send_json({
            'timestamp': timestamp
        })
        timestamp += 5
        await asyncio.sleep(5)
