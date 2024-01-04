from fastapi import WebSocket
from fastapi.websockets import WebSocketDisconnect
from logging import getLogger
from starlette.websockets import WebSocketState

logger = getLogger(__name__)


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def _disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def gracefully_disconnect(
        self, exception: Exception, websocket: WebSocket
    ):
        """Gracefully disconnect and log error in case of exception.

        Args:
            exception: `Exception` that occured
            websocket: `WebSocket` instance
        """
        if isinstance(exception, WebSocketDisconnect):
            return

        elif websocket.client_state == WebSocketState.DISCONNECTED:
            self._disconnect(websocket)
            logger.info(f"""
                Connection closed for chat: {websocket.path_params['id']}
            """)
        else:
            logger.error(exception)
            await websocket.send_json({
                "status": "error",
                "message": "ERROR: An error was encountered. Reload required"
            })
