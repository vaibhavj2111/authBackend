from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://neondb_owner:npg_XO2lLEfz6enb@ep-icy-queen-a500ll1s-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require"

Base= declarative_base()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Database:
    def __init__(self):
        self.session = SessionLocal()

    def get_db(self):
        try:
            yield self.session
        finally:
            self.session.close()
