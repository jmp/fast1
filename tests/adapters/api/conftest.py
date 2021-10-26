from typing import Optional

from _pytest.fixtures import fixture
from starlette.testclient import TestClient

from app.dependencies import Dependencies, get_dependencies
from app.domain.circuit import Circuit
from app.main import app
from app.ports.spi.get_circuit_port import GetCircuitPort
from app.services.circuit_service import CircuitService
from tests.domain.circuits import monza


def _get_fake_dependencies() -> Dependencies:
    class InMemoryCircuitRepository(GetCircuitPort):
        def get_circuit(self, ref: str) -> Optional[Circuit]:
            return monza if ref == monza.ref else None

    return Dependencies(circuit_service=CircuitService(InMemoryCircuitRepository()))


app.dependency_overrides[get_dependencies] = _get_fake_dependencies


@fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)
