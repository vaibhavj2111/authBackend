from fastapi import HTTPException
from models import User
from database import Database
from security import Security
from schemas import UserCreate
from sqlalchemy.exc import SQLAlchemyError

class AuthService:

    def __init__(self):
        self.db = db

    def register(self, user_data: UserCreate):
        try:
            if self.db.query(User).filter(User.email == user_data.email).first():
                raise HTTPException(status_code=400, detail="Email already registered")
        
            hashedPassword = Security.hashPassword(user_data.password)
            user = User(name = user_data.name, email = user_data.email, password=hashedPassword)

            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)   

            return{"message": "User registered successfully"}

        except SQLAlchemyError as e:g
            self.db.rollback()
            raise HTTPException(status_code=400, detail="ErrorSQL registering user")

        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Error registering user")


    def login(self, user_data: UserCreate):
        try:
            db_user = self.db.query(User).filter(User.email == user_data.email).first()
            if not db_user or not Security.verifyPassword(user_data.password, db_user.hashedPassword):
                raise HTTPException(status_code=400, detail="Invalid credentials")
            
            access_token = Security.createAccessToken({"sub": db_user.email})
            return {"access_token": access_token, "token_type": "bearer"}
    
        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="ErrorSQL registering user.... error: {e}")

        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Error registering user.... error: {e}")