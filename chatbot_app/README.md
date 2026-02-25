# Flask AI Chatbot (End-to-End)

This project provides an end-to-end Python chatbot backend that can integrate with any application through HTTP APIs.

## Features
- User management
- Chat sessions and message history
- AI response generation with provider abstraction
  - `rule_based` provider for offline/local environments
  - `openai` provider for production-grade LLM responses
- Integration event ingestion endpoint for external apps/webhooks
- SQLAlchemy ORM models for persistence

## Recommended Database
For production use, configure PostgreSQL. For quick local setup, SQLite is enabled by default.

- Local default: `sqlite:///chatbot.db`
- Production recommendation: PostgreSQL (optionally with pgvector for embeddings)

## Quick Start
```bash
cd chatbot_app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m chatbot_app.app
```

Server runs on `http://localhost:5000`.

## Environment Variables
- `DATABASE_URL` (default: `sqlite:///chatbot.db`)
- `LLM_PROVIDER` (`rule_based` or `openai`)
- `OPENAI_API_KEY` (required if `LLM_PROVIDER=openai`)
- `OPENAI_MODEL` (default: `gpt-4o-mini`)
- `CHATBOT_NAME` (default: `FlaskBot`)

## API Flow (End-to-End)
1. Create user
2. Create session
3. Send chat message
4. Fetch chat history
5. Push integration events from external apps

### 1) Create user
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"email":"alex@example.com", "name":"Alex"}'
```

### 2) Create session
```bash
curl -X POST http://localhost:5000/sessions \
  -H "Content-Type: application/json" \
  -d '{"user_id":1, "title":"Product Questions"}'
```

### 3) Chat
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":1, "message":"Hello, what database should I use?"}'
```

### 4) Message history
```bash
curl http://localhost:5000/sessions/1/messages
```

### 5) Integration events
```bash
curl -X POST http://localhost:5000/integrations/events \
  -H "Content-Type: application/json" \
  -d '{
    "source_app":"crm",
    "event_type":"new_lead",
    "payload":{"lead_id":"L-1001", "priority":"high"}
  }'
```

## Notes for integrating with Flask apps
If you already have an existing Flask application, copy the blueprint/routes and service layer into your app package and initialize SQLAlchemy in your app factory.
