from sqlalchemy.orm import Session
from nicholascooks.orm import models


def get_or_create_user(db: Session, userid: str) -> models.UserORM:
    user = db.query(models.UserORM).filter(models.UserORM.userid == userid).first()
    if user:
        return user
    else:
        user = models.UserORM(userid=userid)
        db.add(user)
        db.commit()
        return user
