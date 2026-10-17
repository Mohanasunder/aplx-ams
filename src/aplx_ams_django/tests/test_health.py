"""
FEAT-000-ACC TST-001 AC-2
Test that GET /api/health/ returns HTTP 200 with body {"status": "ok"}.
This test is red until health.py is implemented and the URL is registered.
No database access needed — health check is a pure view.
"""

from rest_framework.test import APIClient


def test_health_returns_200() -> None:
    """TST-001 AC-2 — health endpoint returns 200 and {"status": "ok"}."""
    client = APIClient()
    response = client.get("/api/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
