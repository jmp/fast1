from typing import Any

from fastapi.testclient import TestClient
from pytest import mark
from pytest_bdd import given, scenario, then, when

from app.main import app
from tests.fixtures.circuits import monza


@mark.acceptance
@scenario(
    "features/circuits.feature",
    "Getting the details of a single circuit",
)  # type: ignore
def test_getting_single_circuit_details() -> None:
    pass


@given("I'm a user", target_fixture="client")  # type: ignore
def client() -> TestClient:
    return TestClient(app)


@given("I have a reference to a circuit", target_fixture="ref")  # type: ignore
def ref() -> str:
    return monza.ref


@when("I submit a request for the circuit", target_fixture="response")  # type: ignore
def submit_request(client: TestClient, ref: str) -> Any:
    return client.get(f"/circuits/{ref}")


@then("I should receive the circuit details")  # type: ignore
def circuit_details_received(response: Any) -> None:
    assert "ref" in response.json()
