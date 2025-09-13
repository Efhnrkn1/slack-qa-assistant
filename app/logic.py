import os

def _heuristics(diff: str) -> list[str]:
    ideas = []
    d = diff.lower()
    if "endpoint" in d:
        ideas.append("API contract tests for new/updated endpoint")
    if "schema" in d or "migration" in d or "db" in d:
        ideas.append("DB migration tests and rollback validation")
    if not ideas:
        ideas = ["Unit tests", "Integration tests", "Negative tests"]
    return ideas

def _enrich_with_llm(base: list[str]) -> list[str] | None:
    if not os.getenv("OPENAI_API_KEY"):
        return None
    return base + ["Property-based tests", "Cross-check with incident runbooks"]

def suggest_tests(repo: str, diff: str) -> dict:
    base = _heuristics(diff)
    enriched = _enrich_with_llm(base)
    return {
        "repo": repo,
        "diff_summary": diff[:200],
        "suggested_tests": enriched or base,
        "llm_enriched": enriched is not None,
    }
