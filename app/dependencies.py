from dataclasses import dataclass
from typing import Callable

from .adapters.spi.persistence.repositories.circuit_repository import CircuitRepository
from .ports.api.get_circuit_use_case import GetCircuitUseCase
from .services.circuit_service import CircuitService


@dataclass(frozen=True)
class Dependencies:
    get_circuit_use_case: GetCircuitUseCase


def _create_circuit_service() -> CircuitService:
    repository = CircuitRepository()
    service = CircuitService(repository)
    return service


def _create_dependencies() -> Callable[[], Dependencies]:
    circuit_service = _create_circuit_service()
    dependencies = Dependencies(
        get_circuit_use_case=circuit_service,
    )
    return lambda: dependencies


get_dependencies = _create_dependencies()
