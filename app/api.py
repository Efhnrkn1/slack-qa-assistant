from fastapi import FastAPI
from pydantic import BaseModel
from .logic import suggest_tests

app = FastAPI(title="Slack QA Assistant API", version="0.1.0")

class Request(BaseModel):
    repo: str
    diff: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/suggest-tests")
def suggest(req: Request):
    return {"tool": "qa_suggester", **suggest_tests(req.repo, req.diff)}
