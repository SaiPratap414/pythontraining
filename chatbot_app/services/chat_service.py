from __future__ import annotations

from dataclasses import dataclass

from ..extensions import db
from ..models import ChatSession, Message
from .llm import LLMProvider


@dataclass
class ChatResult:
    session_id: int
    user_message_id: int
    assistant_message_id: int
    assistant_reply: str
    provider: str


class ChatService:
    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def send_message(self, session: ChatSession, user_text: str) -> ChatResult:
        user_message = Message(
            session_id=session.id,
            role="user",
            content=user_text,
            provider=getattr(self.llm, "provider_name", "unknown"),
        )
        db.session.add(user_message)
        db.session.flush()

        llm_reply = self.llm.generate(user_text)

        assistant_message = Message(
            session_id=session.id,
            role="assistant",
            content=llm_reply.content,
            provider=llm_reply.provider,
        )
        db.session.add(assistant_message)
        db.session.commit()

        return ChatResult(
            session_id=session.id,
            user_message_id=user_message.id,
            assistant_message_id=assistant_message.id,
            assistant_reply=assistant_message.content,
            provider=assistant_message.provider,
        )
