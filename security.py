from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta


SECRET_KEY = "password"

class Security:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hashPassword(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def verifyPassword(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def createAccessToken(cls, data:dict, expires_delta: timedelta) -> str:
        to_encode = data.copy()
        expire = datetime.now() + expires_delta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")