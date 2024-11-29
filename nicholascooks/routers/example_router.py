from fastapi import Depends, APIRouter

from nicholascooks.orm import models
from nicholascooks.utils.dependencies import get_db, get_current_user
from sqlalchemy.orm import Session

from nicholascooks.utils.exceptions import ExampleNotFoundException

from nicholascooks.utils.logger import log

import random

router = APIRouter(
    prefix="/examples",
    tags=["Examples"],
)


# unprotected route
@router.get("/", include_in_schema=False)
@router.get("")
def get_questions_list(
    db: Session = Depends(get_db),
) -> str:
    return "working"
