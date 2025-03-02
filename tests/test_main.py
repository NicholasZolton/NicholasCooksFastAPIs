# to test run `pytest` in the terminal
from typing import Annotated, Optional
from fastapi import Depends, HTTPException, Header
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import pytest
from fastapi.testclient import TestClient
from starlette.types import HTTPExceptionHandler
from nicholascooks.app import app
from nicholascooks.utils.dependencies import get_current_user, get_db
from sqlalchemy.orm import sessionmaker
from nicholascooks.orm import models
from nicholascooks.orm.models import *
from sqlalchemy import create_engine

from nicholascooks.utils.exceptions import UnauthenticatedException

TEST_USER_ID = "testing|123"


engine = create_engine("sqlite:///:memory:")
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
SQLModel.metadata.create_all(engine)


@pytest.fixture()
def session():
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    # Dependency overrides
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    # hacky, but makes testing easier - just use invalid token for testing
    # invalid permissions
    def override_get_current_user(
        Authorization: Annotated[str | None, Header()] = None,
    ):
        token = Authorization
        if token is None:
            return models.User(auth0_id="testuser")
        elif token == "invalid":
            raise HTTPException(status_code=403)
        else:
            return models.User(auth0_id="testuser")

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_current_user

    yield TestClient(app)


def test_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "http://testserver/docs"}


def test_user_info(client: TestClient):
    response = client.get("/users/info")
    assert response.status_code == 200
    response = client.get("/users/info", headers={"Authorization": f"invalid"})
    assert response.status_code == 403
    response = client.get(
        "/users/info", headers={"Authorization": f"Bearer {TEST_USER_ID}"}
    )
    assert response.status_code == 200
