# to test run `pytest` in the terminal
from fastapi import Depends
from fastapi.testclient import TestClient
from nicholascooks.app import app
from nicholascooks.utils.dependencies import get_current_user, get_db
from nicholascooks.utils.crud import get_or_create_user
from sqlalchemy.orm import Session

TEST_USER_ID = "testing|123"


def override_get_current_user(
    db: Session = Depends(get_db),
):
    return get_or_create_user(db=db, userid=TEST_USER_ID)


client = TestClient(app)


def test_main():
    app.dependency_overrides[get_current_user] = override_get_current_user

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "http://127.0.0.1:8000/docs"}
