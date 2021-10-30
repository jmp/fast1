from typing import Optional

from app.adapters.spi.entities.circuit_entity import CircuitEntity
from app.adapters.spi.session import db_session
from app.domain.circuit import Circuit
from app.ports.spi import GetCircuitPort


class CircuitRepository(GetCircuitPort):
    def get_circuit(self, ref: str) -> Optional[Circuit]:
        session = db_session.get()
        entity: Optional[CircuitEntity] = (
            session.query(CircuitEntity)
            .filter(CircuitEntity.circuit_ref == ref)
            .first()
        )
        if entity is not None:
            return entity.to_domain_model()
        return None
