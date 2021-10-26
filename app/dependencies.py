from dataclasses import dataclass
from typing import Callable

from .adapters.spi.persistence.repositories.circuit_repository import CircuitRepository
from .services.circuit_service import CircuitService


@dataclass(frozen=True)
class Dependencies:
    circuit_service: CircuitService


def _create_circuit_service() -> CircuitService:
    repository = CircuitRepository()
    service = CircuitService(repository)
    return service


def _create_dependencies() -> Callable[[], Dependencies]:
    dependencies = Dependencies(
        circuit_service=_create_circuit_service(),
    )
    return lambda: dependencies


get_dependencies = _create_dependencies()
