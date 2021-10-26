from app.adapters.spi.persistence.repositories.circuit_repository import (
    CircuitRepository,
)
from tests.domain.circuits import monza


def test_get_circuit_returns_circuit_if_it_exists() -> None:
    repository = CircuitRepository()
    circuit = repository.get_circuit("monza")
    assert circuit == monza


def test_get_circuit_returns_none_if_it_does_not_exist() -> None:
    repository = CircuitRepository()
    circuit = repository.get_circuit("does_not_exist")
    assert circuit is None
