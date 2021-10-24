from fastapi.testclient import TestClient


def test_smoke(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 404
