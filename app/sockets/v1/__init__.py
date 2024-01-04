from fastapi.routing import APIRouter
from app.sockets.v1.conversation import conversation_router
from app.sockets.v1.rag import rag_router

sockets = APIRouter(prefix="/ws/v1")
sockets.include_router(conversation_router)
sockets.include_router(rag_router)
