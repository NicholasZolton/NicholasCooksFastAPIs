from sqlalchemy.orm import Session
from sqlmodel import select
from nicholascooks.orm import models


def get_or_create_user(db: Session, userid: str) -> models.User:
    stmt = select(models.User).where(models.User.auth0_id == userid)
    user = db.scalars(stmt).first()
    if user:
        return user
    else:
        user = models.User(auth0_id=userid)
        db.add(user)
        db.commit()
        return user
