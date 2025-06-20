from fastapi import FastAPI
from app.routes import chat

app = FastAPI(title="FinBot API")

app.include_router(chat.router)