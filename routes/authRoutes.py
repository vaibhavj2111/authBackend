from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from models import User
from database import Database
from services.authServices import AuthService
from schemas import UserCreate

router = APIRouter()

db_instance = Database()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/register")
async def register(user_data: UserCreate, db: Session = Depends(db_instance.get_db)):
    return AuthService().register(user_data)

@router.post("/login")
async def login(user_data: UserCreate, db: Session = Depends(db_instance.get_db)):
    return AuthService().login(user_data)
