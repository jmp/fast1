from typing import Optional

from app.domain.circuit import Circuit
from app.ports.spi.get_circuit_port import GetCircuitPort

from ..entities.circuit_entity import CircuitEntity
from ..session import db_session


class CircuitRepository(GetCircuitPort):
    def get_circuit(self, ref: str) -> Optional[Circuit]:
        session = db_session.get()
        if session is None:
            return None
        entity: Optional[CircuitEntity] = (
            session.query(CircuitEntity)
            .filter(CircuitEntity.circuit_ref == ref)
            .first()
        )
        if entity is not None:
            return entity.to_domain_model()
        return None
