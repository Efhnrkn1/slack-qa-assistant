# Slack QA Assistant

A lightweight Slack app that suggests **test cases for pull requests / diffs** using heuristics with optional LLM enrichment. 

- **Slash command** → `/suggest-tests <summary of change>`
- **HTTP API** → `POST /suggest-tests` with repo + diff summary

## Why this project
Engineers often spend time re-deriving the same test ideas for common change types (new endpoints, DB schema changes, auth). This assistant proposes a quick **starter set of tests**.

## Quick start (API only)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.api:app --reload
```

Example request:
```bash
curl -X POST http://127.0.0.1:8000/suggest-tests   -H "Content-Type: application/json"   -d '{"repo":"payments-service","diff":"added endpoint /transactions and a schema change"}'
```

## Slack app setup (optional)
- Create a Slack app → add `/suggest-tests` slash command → point to `/slack/events`
- Set env vars: `SLACK_SIGNING_SECRET`, `SLACK_BOT_TOKEN`, optional `OPENAI_API_KEY`
- Run: `python -m app.bolt_app`
