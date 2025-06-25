from fastapi import FastAPI
from app.routes import chat
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI(title="FinBot API")

app.include_router(chat.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)