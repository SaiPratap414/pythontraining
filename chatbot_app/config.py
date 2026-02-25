from __future__ import annotations

import os


class Config:
    """Application configuration with sane local defaults."""

    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///chatbot.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "rule_based")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    CHATBOT_NAME = os.getenv("CHATBOT_NAME", "FlaskBot")
