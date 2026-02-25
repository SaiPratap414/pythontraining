from chatbot_app.app import create_app
from chatbot_app.extensions import db


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LLM_PROVIDER = "rule_based"
    CHATBOT_NAME = "TestBot"


import pytest


@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
    with app.test_client() as client:
        yield client


def test_end_to_end_chat_flow(client):
    create_user = client.post("/users", json={"email": "jane@example.com", "name": "Jane"})
    assert create_user.status_code == 201
    user_id = create_user.get_json()["id"]

    create_session = client.post("/sessions", json={"user_id": user_id, "title": "Support"})
    assert create_session.status_code == 201
    session_id = create_session.get_json()["session_id"]

    chat = client.post("/chat", json={"session_id": session_id, "message": "hello"})
    assert chat.status_code == 200
    body = chat.get_json()
    assert body["provider"] == "rule_based"
    assert "Hello" in body["assistant_reply"]

    history = client.get(f"/sessions/{session_id}/messages")
    assert history.status_code == 200
    messages = history.get_json()["messages"]
    assert len(messages) == 2
    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"


def test_integration_event_ingestion(client):
    response = client.post(
        "/integrations/events",
        json={
            "source_app": "helpdesk",
            "event_type": "ticket_created",
            "payload": {"ticket_id": "T100"},
        },
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["source_app"] == "helpdesk"
    assert data["event_type"] == "ticket_created"
