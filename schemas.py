from pydantic import BaseModel #EmailStr

class UserCreate(BaseModel):
    id: int
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str