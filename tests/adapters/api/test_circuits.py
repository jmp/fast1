from fastapi.testclient import TestClient


def test_get_circuit(client: TestClient) -> None:
    response = client.get("/circuits/monza")
    assert response.status_code == 200
    assert response.json() == {
        "ref": "monza",
        "name": "Autodromo Nazionale di Monza",
        "location": "Monza",
        "country": "Italy",
        "latitude": 45.6156,
        "longitude": 9.28111,
        "altitude": 162,
        "url": "http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza",
    }
