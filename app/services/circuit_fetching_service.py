from typing import Optional

from app.domain.circuit import Circuit
from app.ports.api.get_circuit_use_case import GetCircuitUseCase
from app.ports.spi.get_circuit_port import GetCircuitPort


class CircuitFetchingService(GetCircuitUseCase):
    def __init__(self, get_circuit: GetCircuitPort):
        self.get_circuit_port = get_circuit

    def get_circuit(self, ref: str) -> Optional[Circuit]:
        return self.get_circuit_port.get_circuit(ref)
