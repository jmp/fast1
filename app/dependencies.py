from typing import Optional

from .domain.circuit import Circuit
from .ports.spi.get_circuit_port import GetCircuitPort
from .services.circuit_service import CircuitService


def _create_circuit_service() -> CircuitService:
    class DummyGetCircuitAdapter(GetCircuitPort):
        def get_circuit(self, ref: str) -> Optional[Circuit]:
            if ref == "monza":
                return Circuit(
                    id=14,
                    ref="monza",
                    name="Autodromo Nazionale di Monza",
                    location="Monza",
                    country="Italy",
                    latitude=45.6156,
                    longitude=9.28111,
                    altitude=162,
                    url="http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza",
                )
            return None

    adapter = DummyGetCircuitAdapter()
    service = CircuitService(adapter)
    return service


circuit_service = _create_circuit_service()
