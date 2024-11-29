from typing import Optional
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from nicholascooks.utils.database import SessionLocal
from nicholascooks.utils.exceptions import (
    UnauthorizedException,
    UnauthenticatedException,
)
from nicholascooks.utils.crud import get_or_create_user
from nicholascooks.orm import models
from sqlalchemy.orm import Session
import os
import jwt


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer()),
    db: Session = Depends(get_db),
) -> models.UserORM:
    if token is None:
        raise UnauthenticatedException

    try:
        jwks_url = f"https://{os.environ['AUTH0_DOMAIN']}/.well-known/jwks.json"
        jwks_client = jwt.PyJWKClient(jwks_url)
        signing_key = jwks_client.get_signing_key_from_jwt(token.credentials).key
    except jwt.exceptions.PyJWKClientError as error:
        raise UnauthorizedException(str(error))
    except jwt.exceptions.DecodeError as error:
        raise UnauthorizedException(str(error))

    try:
        payload = jwt.decode(
            token.credentials,
            signing_key,
            algorithms=os.environ["AUTH0_ALGORITHMS"],  # type: ignore
            audience=os.environ["AUTH0_API_AUDIENCE"],
            issuer=os.environ["AUTH0_ISSUER"],
        )
    except Exception as error:
        raise UnauthorizedException(str(error))

    # find the user in the database from the 'sub' claim
    # if the user does not exist, create them
    user = get_or_create_user(db, payload["sub"])

    # if the payload contains an email, update the user's email - MUST BE UNIQUE WITH STRIPE
    # if payload.get("email"):
    #     if not str(user.account_email) or user.account_email != payload["email"]:
    #         user.account_email = payload["email"]
    #         db.commit()

    # if payload.get("stripe_customer"):
    #     if (
    #         not user.stripe_customer  # type: ignore
    #         or user.stripe_customer != payload["stripe_customer"]
    #     ):
    #         user.stripe_customer = payload["stripe_customer"]
    #         db.commit()
    return user


# def check_active_stripe_subscription(current_user: models.UserORM, db: Session):
#     stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
#     sublist = stripe.Subscription.list(
#         customer=str(current_user.stripe_customer), status="active"
#     )
#       pass
