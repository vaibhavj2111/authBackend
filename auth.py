from datetime import datetime, timedelta
import jwt
from fastapi import Depends, HTTPException, status

SECRET_KEY = "password"

def create_Access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.now(datetime.time) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

@router.post("/login")

def login(user:UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(user.password, user.hashed_password):
        raise HTTPException(status_code=404, detail="Incorrect password")
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_Access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}