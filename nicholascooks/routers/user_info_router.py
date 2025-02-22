from fastapi import Depends, APIRouter

from nicholascooks.orm import models
from nicholascooks.utils.dependencies import get_current_user, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users/info",
    tags=["info"],
)


# protected route (depends on get_current_user)
@router.get("/", include_in_schema=False)
@router.get("")
def get_user_info(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    return current_user
