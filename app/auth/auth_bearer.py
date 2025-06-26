from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials 
from .auth_handler import decode_jwt 

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            user_id = decode_jwt(credentials.credentials)
            if user_id is None:
                raise HTTPException(status_code=403, detail="Invalid or expired token")
            return user_id
        raise HTTPException(status_code=403, detail="Invalid authorization")