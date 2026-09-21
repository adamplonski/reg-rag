from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# health
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["ok"]
    assert data["version"] == "dev"
    assert "uptime_seconds" in data


# echo
def test_echo():
    response = client.get("/echo/test123")
    assert response.status_code == 200
    assert response.json()["response"] == "test123"

    response = client.get("/echo/" + "-" * 501)
    assert response.status_code == 422

    response = client.get("/echo/" + "-" * 500)
    assert response.status_code == 200

    response = client.get("/echo/%20wumbo%20")
    assert response.json()["response"] == "wumbo"
    assert response.status_code == 200
