from sqlalchemy import String, Integer, Column
from database import Base
# from sqlalchemy.orm import unique, relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name= Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

