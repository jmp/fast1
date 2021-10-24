from typing import Optional

from app.domain.circuit import Circuit
from app.ports.api.get_circuit_use_case import GetCircuitUseCase
from app.ports.spi.get_circuit_port import GetCircuitPort
from app.services.circuit_service import CircuitService


def test_get_circuit_returns_circuit_if_it_exists(monza: Circuit) -> None:
    class GetCircuitAdapter(GetCircuitPort):
        def get_circuit(self, ref: str) -> Optional[Circuit]:
            return monza

    service: GetCircuitUseCase = CircuitService(GetCircuitAdapter())
    circuit = service.get_circuit("monza")
    assert circuit == monza


def test_get_circuit_returns_none_if_circuit_does_not_exist() -> None:
    class GetCircuitAdapter(GetCircuitPort):
        def get_circuit(self, ref: str) -> Optional[Circuit]:
            return None

    service: GetCircuitUseCase = CircuitService(GetCircuitAdapter())
    circuit = service.get_circuit("does_not_exist")
    assert circuit is None
