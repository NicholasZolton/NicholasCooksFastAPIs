import pytest
from fastapi.testclient import TestClient
from nicholascooks.app import app
from nicholascooks.utils.dependencies import get_current_user
from tests.test_main import (
    client,
    TEST_USER_ID,
)


# def test_get_example_list(client: TestClient):
#     app.dependency_overrides[get_current_user] = override_get_current_user
#     app.dependency_overrides[get_db] = override_get_db
#
#     response = client.get("/examples")
#     assert response.status_code == 200
#     assert len(response.json()) > 0
