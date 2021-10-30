from typing import Optional

from app.domain.circuit import Circuit
from app.ports.spi import GetCircuitPort
from app.services.circuit_service import CircuitService
from tests.fixtures.circuits import monza


def test_get_circuit_returns_circuit_if_it_exists() -> None:
    adapter = _build_get_circuit_adapter(monza)
    service = CircuitService(adapter)
    circuit = service.get_circuit(monza.ref)
    assert circuit == monza


def test_get_circuit_returns_none_if_circuit_does_not_exist() -> None:
    adapter = _build_get_circuit_adapter(None)
    service = CircuitService(adapter)
    circuit = service.get_circuit("does_not_exist")
    assert circuit is None


def _build_get_circuit_adapter(circuit: Optional[Circuit]) -> GetCircuitPort:
    class GetCircuitAdapter(GetCircuitPort):
        def get_circuit(self, ref: str) -> Optional[Circuit]:
            return circuit

    return GetCircuitAdapter()
