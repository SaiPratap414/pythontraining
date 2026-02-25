from __future__ import annotations

from datetime import datetime

from .extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    sessions = db.relationship("ChatSession", backref="user", lazy=True, cascade="all, delete-orphan")


class ChatSession(db.Model):
    __tablename__ = "chat_sessions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, default="New Session")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    messages = db.relationship("Message", backref="session", lazy=True, cascade="all, delete-orphan")


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey("chat_sessions.id"), nullable=False, index=True)
    role = db.Column(db.String(20), nullable=False)  # system/user/assistant
    content = db.Column(db.Text, nullable=False)
    provider = db.Column(db.String(50), nullable=False, default="rule_based")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class IntegrationEvent(db.Model):
    __tablename__ = "integration_events"

    id = db.Column(db.Integer, primary_key=True)
    source_app = db.Column(db.String(120), nullable=False)
    event_type = db.Column(db.String(120), nullable=False)
    payload = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
