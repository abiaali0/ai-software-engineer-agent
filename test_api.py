from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze_issue() -> None:
    response = client.post(
        "/analyze",
        json={
            "title": "Add CSV export",
            "body": "Users need to export filtered reports as CSV.",
            "repository_path": ".",
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["issue"]["title"] == "Add CSV export"
    assert "csv" in data["issue"]["keywords"]
    assert data["implementation_plan"]
    assert "Summary" in data["pull_request_summary"]
