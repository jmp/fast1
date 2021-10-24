from app.domain.circuit import Circuit
from app.ports.api.get_circuit_use_case import GetCircuitUseCase
from app.ports.spi.get_circuit_port import GetCircuitPort
from app.services.circuit_fetching_service import CircuitFetchingService


def test_get_circuit_returns_circuit_if_it_exists() -> None:
    expected_circuit = Circuit(
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

    class GetCircuitAdapter(GetCircuitPort):
        def get_circuit(self, ref: str) -> Circuit:
            return expected_circuit

    service: GetCircuitUseCase = CircuitFetchingService(GetCircuitAdapter())
    circuit: Circuit = service.get_circuit("monza")
    assert circuit == expected_circuit
