from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings as s
# import mysql.connector
# import time

SQLALCHEMY_DATABASE_URL = f"mysql://{s.db_username}:{s.db_password}@{s.db_host}/{s.db_dbname}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def test_connect_db():
#     while True:
#         try:
#             config = {
#                 'user': 'fastapi',
#                 'password': 'Polyglot98$$',
#                 'host': '127.0.0.1',
#                 'database': 'fastapi',
#                 'raise_on_warnings': True
#             }
#             conn = mysql.connector.connect(**config)
#             cursor = conn.cursor()
#             print("Database connection was successful")
#             break
#         except Exception as error:
#             print("Connection to database failed")
#             print("Error: ", error)
#             time.sleep(2)        