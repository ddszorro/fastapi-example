from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings as s
# import mysql.connector
# import time

# SQLALCHEMY_DATABASE_URL = f"mysql://{s.db_username}:{s.db_password}@{s.db_host}/{s.db_dbname}"
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{s.db_username}:{s.db_password}@{s.db_host}/{s.db_dbname}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

   