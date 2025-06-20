from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.openai_service import generate_advice

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest):
    reply = await generate_advice(request.message)
    return ChatResponse(reply=reply)