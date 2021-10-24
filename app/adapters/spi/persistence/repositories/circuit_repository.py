from typing import Optional

from app.domain.circuit import Circuit
from app.ports.spi.get_circuit_port import GetCircuitPort

from ..entities.circuit_entity import CircuitEntity


class CircuitRepository(GetCircuitPort):
    def get_circuit(self, ref: str) -> Optional[Circuit]:
        if ref == "monza":
            return CircuitEntity(
                circuit_id=14,
                circuit_ref="monza",
                name="Autodromo Nazionale di Monza",
                location="Monza",
                country="Italy",
                lat=45.6156,
                lng=9.28111,
                alt=162,
                url="http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza",
            ).to_domain_model()
        return None
