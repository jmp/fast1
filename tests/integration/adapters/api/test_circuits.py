from fastapi.testclient import TestClient
from pytest import mark


@mark.integration
def test_get_circuit(client: TestClient) -> None:
    response = client.get("/circuits/monza")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Autodromo Nazionale di Monza",
        "location": "Monza",
        "country": "Italy",
        "latitude": 45.6156,
        "longitude": 9.28111,
        "altitude": 162,
        "url": "http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza",
    }


@mark.integration
def test_get_circuit_returns_404_if_not_found(client: TestClient) -> None:
    response = client.get("/circuits/does_not_exist")
    assert response.status_code == 404
