from typing import Any

from fastapi.testclient import TestClient
from pytest import mark
from pytest_bdd import given, scenario, then, when

from app.main import app
from tests.unit.domain.circuits import monza


@mark.acceptance
@scenario("circuits.feature", "Getting the details of a single circuit")  # type: ignore
def test_getting_single_circuit_details() -> None:
    pass


@given("I'm a user", target_fixture="client")  # type: ignore
def client() -> TestClient:
    return TestClient(app)


@given("I have a reference to a circuit", target_fixture="ref")  # type: ignore
def ref() -> str:
    return monza.ref


@when("I submit a request for the circuit", target_fixture="details")  # type: ignore
def submit_request(client: TestClient, ref: str) -> Any:
    return client.get(f"/circuits/{ref}")


@then("I should receive the details for the circuit")  # type: ignore
def circuit_details_received(details: Any) -> None:
    assert details.json() == {
        "name": "Autodromo Nazionale di Monza",
        "location": "Monza",
        "country": "Italy",
        "latitude": 45.6156,
        "longitude": 9.28111,
        "altitude": 162,
        "url": "http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza",
    }
