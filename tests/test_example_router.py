from nicholascooks.app import app
from nicholascooks.utils.dependencies import get_current_user
from tests.test_main import override_get_current_user, client, TEST_USER_ID


def test_get_questions_list():
    response = client.get("/examples")
    assert response.status_code == 200
    assert len(response.json()) > 0
