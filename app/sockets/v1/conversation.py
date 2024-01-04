from fastapi import APIRouter, WebSocket
from app.sockets.connection_manager import ConnectionManager

conversation_router = APIRouter(prefix="/conversation")
connection_manager = ConnectionManager()


@conversation_router.websocket("")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")

    except Exception as e:
        await connection_manager.gracefully_disconnect(e, websocket)
