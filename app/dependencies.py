from .adapters.spi.persistence.repositories.circuit_repository import CircuitRepository
from .services.circuit_service import CircuitService


def _create_circuit_service() -> CircuitService:
    repository = CircuitRepository()
    service = CircuitService(repository)
    return service


circuit_service = _create_circuit_service()
