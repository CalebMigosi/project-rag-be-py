from websockets import WebSocket
from typing import AsyncIterator


class StreamStringToWebSocket:
    """Stream the output directly to the websocket as string"""
    def __init__(self, socket: WebSocket):
        self.socket = socket

    async def __call__(self, input: AsyncIterator[str]):
        async for chunk in input:
            self.socket.send(chunk)
