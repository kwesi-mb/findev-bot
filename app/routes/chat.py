from fastapi import APIRouter, Depends 
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.openai_service import generate_advice
from app.auth.auth_bearer import JWTBearer 

router = APIRouter()

@router.post("/chat", response_model=ChatResponse, dependencies=[Depends(JWTBearer())])
async def chat_with_bot(request: ChatRequest):
    reply = await generate_advice(request.message)
    return ChatResponse(reply=reply)