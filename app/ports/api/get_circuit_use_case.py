from typing import Optional

from app.domain.circuit import Circuit


class GetCircuitUseCase:
    def get_circuit(self, ref: str) -> Optional[Circuit]:
        raise NotImplementedError
