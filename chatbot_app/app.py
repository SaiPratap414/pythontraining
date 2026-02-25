from __future__ import annotations

from flask import Flask, jsonify, request

from .config import Config
from .extensions import db
from .models import ChatSession, IntegrationEvent, Message, User
from .services.chat_service import ChatService
from .services.llm import get_provider


def create_app(config_object=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.get("/health")
    def health_check():
        return jsonify({"status": "ok", "chatbot": app.config["CHATBOT_NAME"]})

    @app.post("/users")
    def create_user():
        payload = request.get_json(force=True)
        email = payload.get("email")
        name = payload.get("name")
        if not email or not name:
            return jsonify({"error": "email and name are required"}), 400

        existing = User.query.filter_by(email=email).first()
        if existing:
            return jsonify({"error": "user already exists", "user_id": existing.id}), 409

        user = User(email=email, name=name)
        db.session.add(user)
        db.session.commit()

        return jsonify({"id": user.id, "email": user.email, "name": user.name}), 201

    @app.post("/sessions")
    def create_session():
        payload = request.get_json(force=True)
        user_id = payload.get("user_id")
        title = payload.get("title", "New Session")
        if not user_id:
            return jsonify({"error": "user_id is required"}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "user not found"}), 404

        chat_session = ChatSession(user_id=user_id, title=title)
        db.session.add(chat_session)
        db.session.commit()

        return (
            jsonify(
                {
                    "session_id": chat_session.id,
                    "user_id": chat_session.user_id,
                    "title": chat_session.title,
                }
            ),
            201,
        )

    @app.get("/sessions/<int:session_id>/messages")
    def get_messages(session_id: int):
        session = ChatSession.query.get(session_id)
        if not session:
            return jsonify({"error": "session not found"}), 404

        messages = (
            Message.query.filter_by(session_id=session_id)
            .order_by(Message.created_at.asc())
            .all()
        )
        return jsonify(
            {
                "session_id": session.id,
                "messages": [
                    {
                        "id": message.id,
                        "role": message.role,
                        "content": message.content,
                        "provider": message.provider,
                        "created_at": message.created_at.isoformat(),
                    }
                    for message in messages
                ],
            }
        )

    @app.post("/chat")
    def chat():
        payload = request.get_json(force=True)
        session_id = payload.get("session_id")
        user_message = payload.get("message")

        if not session_id or not user_message:
            return jsonify({"error": "session_id and message are required"}), 400

        session = ChatSession.query.get(session_id)
        if not session:
            return jsonify({"error": "session not found"}), 404

        llm = get_provider(app.config)
        chat_service = ChatService(llm_provider=llm)
        result = chat_service.send_message(session=session, user_text=user_message)

        return jsonify(
            {
                "session_id": result.session_id,
                "assistant_reply": result.assistant_reply,
                "provider": result.provider,
                "message_ids": {
                    "user": result.user_message_id,
                    "assistant": result.assistant_message_id,
                },
            }
        )

    @app.post("/integrations/events")
    def integration_event():
        payload = request.get_json(force=True)
        source_app = payload.get("source_app")
        event_type = payload.get("event_type")
        event_payload = payload.get("payload")

        if not source_app or not event_type or event_payload is None:
            return jsonify({"error": "source_app, event_type and payload are required"}), 400

        event = IntegrationEvent(
            source_app=source_app,
            event_type=event_type,
            payload=event_payload,
        )
        db.session.add(event)
        db.session.commit()

        return (
            jsonify(
                {
                    "event_id": event.id,
                    "source_app": event.source_app,
                    "event_type": event.event_type,
                }
            ),
            201,
        )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
