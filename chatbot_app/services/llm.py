from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class LLMReply:
    content: str
    provider: str


class LLMProvider(Protocol):
    def generate(self, prompt: str) -> LLMReply:
        ...


class RuleBasedLLM:
    """Offline deterministic model useful for local/dev/testing."""

    provider_name = "rule_based"

    def generate(self, prompt: str) -> LLMReply:
        lowered = prompt.lower()
        if "hello" in lowered or "hi" in lowered:
            response = "Hello! How can I help you today?"
        elif "price" in lowered or "cost" in lowered:
            response = "I can help estimate costs. Please share your requirements in detail."
        elif "database" in lowered:
            response = "For most chatbots, PostgreSQL is a strong default, optionally with pgvector."
        else:
            response = f"You said: {prompt}. Can you share more context so I can help better?"
        return LLMReply(content=response, provider=self.provider_name)


class OpenAILLM:
    provider_name = "openai"

    def __init__(self, api_key: str, model: str) -> None:
        from openai import OpenAI

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> LLMReply:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional AI assistant integrated into business apps.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        content = completion.choices[0].message.content or "Sorry, I could not produce an answer."
        return LLMReply(content=content, provider=self.provider_name)


def get_provider(config) -> LLMProvider:
    provider_name = config.get("LLM_PROVIDER", "rule_based")
    if provider_name == "openai":
        api_key = config.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is required when LLM_PROVIDER=openai")
        return OpenAILLM(api_key=api_key, model=config.get("OPENAI_MODEL", "gpt-4o-mini"))

    return RuleBasedLLM()
