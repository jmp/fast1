from fastapi.testclient import TestClient


def test_readiness(client: TestClient) -> None:
    response = client.get("/readiness")
    assert response.status_code == 200
