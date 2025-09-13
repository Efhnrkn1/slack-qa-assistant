import os
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from fastapi import FastAPI, Request
from .logic import suggest_tests

signing_secret = os.getenv("SLACK_SIGNING_SECRET")
bot_token = os.getenv("SLACK_BOT_TOKEN")

app = App(signing_secret=signing_secret, token=bot_token)

@app.command("/suggest-tests")
def handle(ack, respond, command):
    ack()
    text = command.get("text", "changed code")
    result = suggest_tests("repo", text)
    respond(f"Suggested tests: {result['suggested_tests']}")

fastapi = FastAPI()
handler = SlackRequestHandler(app)

@fastapi.post("/slack/events")
async def slack_events(req: Request):
    return await handler.handle(req)
