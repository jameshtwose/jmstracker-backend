from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import os
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

# SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db" #consider using postgresql database in the future
SQLALCHEMY_DATABASE_URL = os.environ["cockroack_db_deta_connect_string"]

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()