from fastapi import APIRouter, WebSocket
from logging import getLogger
from app.sockets.connection_manager import ConnectionManager

rag_router = APIRouter(prefix="/rag")
connection_manager = ConnectionManager()

logger = getLogger(__name__)


@rag_router.websocket("/elastic")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")

    except Exception as e:
        await connection_manager.gracefully_disconnect(e, websocket)
