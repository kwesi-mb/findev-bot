from fastapi import APIRouter, HTTPException 
from app.models.user import User 
from app.auth.auth_handler import sign_jwt
from passlib.hash import bcrypt 


router = APIRouter()
fake_users_db = {}

@router.post("/register")
def register(user: User):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pw = bcrypt.hash(user.password)
    fake_users_db[user.email] = hashed_pw
    return {"msg": "User registered"}


@router.post("/login")
def login(user: User):
    stored_pw = fake_users_db.get(user.email)
    if not stored_pw or not bcrypt.verify(user.password, stored_pw):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": sign_jwt(user.email)}