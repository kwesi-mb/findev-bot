from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 30 

def sign_jwt(user_id: str):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_jwt(token: str):
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        return None 