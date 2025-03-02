from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    auth0_id: str | None = Field(primary_key=True, default=None)
    stripe_customer: str = Field(nullable=True, default="")
    created_at: datetime = Field(default=datetime.now(timezone.utc))


class Example(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    name: str = Field(nullable=False, default="")
