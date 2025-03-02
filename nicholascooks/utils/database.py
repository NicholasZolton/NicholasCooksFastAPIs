from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlmodel import Session
import os
from dotenv import load_dotenv

load_dotenv(override=True)

engine = None
SessionLocal = None
if os.getenv("ASYNC") == "1":
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

    engine = AsyncEngine(create_engine(f"{os.getenv('SQLALCHEMY_DATABASE_URL')}"))
    SessionLocal = sessionmaker(
        engine,  # type: ignore
        autocommit=False,
        class_=AsyncSession,  # type: ignore
    )
elif os.getenv("TURSO") == "1":
    TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
    TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")
    dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

    engine = create_engine(dbUrl, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(bind=engine, autocommit=False, class_=Session)
else:
    engine = create_engine(f"{os.getenv('SQLALCHEMY_DATABASE_URL')}")
    SessionLocal = sessionmaker(bind=engine, autocommit=False, class_=Session)

assert engine is not None
assert SessionLocal is not None


Base = declarative_base()
