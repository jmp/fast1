from asyncio import Protocol
from typing import Optional

from app.domain.circuit import Circuit


class GetCircuitUseCase(Protocol):
    def get_circuit(self, ref: str) -> Optional[Circuit]:
        raise NotImplementedError
