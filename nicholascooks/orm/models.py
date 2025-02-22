from sqlalchemy import Boolean, Column, DateTime, String, ForeignKey, Integer
from nicholascooks.utils.database import Base
from pydantic import BaseModel, ConfigDict
from datetime import datetime, timezone


class UserORM(Base):
    __tablename__ = "users"

    id: Column[int] = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    auth0_id: Column[str] = Column(String, primary_key=True, unique=True)
    stripe_customer: Column[str] = Column(String, nullable=True, default="")
    is_active: Column[bool] = Column(Boolean, default=True)
    created_at: Column[datetime] = Column(DateTime, default=datetime.now(timezone.utc))


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    auth0_sub: str
    stripe_customer: str
    is_active: bool
    created_at: datetime


# class ExampleORM(Base):
#     __tablename__ = "examples"
#
#     id: Column[int] = Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     title: Column[str] = Column(String, nullable=True)
#     description: Column[str] = Column(String, nullable=True)
#     external_link: Column[str] = Column(String, nullable=True)
#
#
# class Example(BaseModel):
#     model_config = ConfigDict(from_attributes=True)
#
#     id: int
#     title: str
#     description: str
#     external_link: str
