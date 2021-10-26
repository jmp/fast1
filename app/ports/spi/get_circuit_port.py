from typing import Optional, Protocol

from app.domain.circuit import Circuit


class GetCircuitPort(Protocol):
    def get_circuit(self, ref: str) -> Optional[Circuit]:
        ...
