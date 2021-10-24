from typing import Optional

from ..entities.circuit_entity import CircuitEntity


class CircuitRepository:
    def get_circuit(self, ref: str) -> Optional[CircuitEntity]:
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
            )
        return None
