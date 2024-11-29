from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv(override=True)

engine = None
if os.getenv("LOCALLY_TESTING") == "1":
    engine = create_engine(
        f'{os.getenv("SQLALCHEMY_DATABASE_URL")}', pool_pre_ping=True
    )  # type: ignore
else:
    engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URL"))  # type: ignore
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
