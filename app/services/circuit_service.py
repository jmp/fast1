from typing import Optional

from app.domain.circuit import Circuit
from app.ports.api.get_circuit_use_case import GetCircuitUseCase
from app.ports.spi.get_circuit_port import GetCircuitPort


class CircuitService(GetCircuitUseCase):
    def __init__(self, get_circuit_adapter: GetCircuitPort):
        self._get_circuit_adapter = get_circuit_adapter

    def get_circuit(self, ref: str) -> Optional[Circuit]:
        return self._get_circuit_adapter.get_circuit(ref)
