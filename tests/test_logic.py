from app.logic import suggest_tests

def test_endpoint_case():
    res = suggest_tests("repo", "added endpoint /users")
    assert any("API contract" in s for s in res["suggested_tests"])

def test_schema_case():
    res = suggest_tests("repo", "ran DB schema migration")
    assert any("migration" in s.lower() for s in res["suggested_tests"])
