from asyncio import Protocol

from app.domain.circuit import Circuit


class GetCircuitUseCase(Protocol):
    def get_circuit(self, ref: str) -> Circuit:
        raise NotImplementedError
