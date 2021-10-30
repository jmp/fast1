from typing import Iterator, Optional

from _pytest.fixtures import fixture
from starlette.testclient import TestClient

from app.adapters.api.dependencies import Dependencies, get_dependencies
from app.adapters.spi.session import SessionLocal
from app.domain.circuit import Circuit
from app.main import app
from app.ports.spi import GetCircuitPort
from app.services.circuit_service import CircuitService
from tests.fixtures.circuits import monza


def _get_fake_dependencies() -> Iterator[Dependencies]:
    class InMemoryCircuitRepository(GetCircuitPort):
        def get_circuit(self, ref: str) -> Optional[Circuit]:
            return monza if ref == monza.ref else None

    circuit_service = CircuitService(InMemoryCircuitRepository())
    session = SessionLocal()
    try:
        yield Dependencies(session=session, get_circuit_use_case=circuit_service)
    finally:
        session.close()


app.dependency_overrides[get_dependencies] = _get_fake_dependencies


@fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)
