from dataclasses import dataclass
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from app.adapters.spi.circuit_repository import CircuitRepository
from app.adapters.spi.session import SessionLocal
from app.ports.api import GetCircuitUseCase
from app.services.circuit_service import CircuitService


@dataclass(frozen=True)
class Dependencies:
    session: Session
    get_circuit_use_case: GetCircuitUseCase


def _create_circuit_service() -> CircuitService:
    repository = CircuitRepository()
    service = CircuitService(repository)
    return service


def _create_dependencies() -> Callable[[], Iterator[Dependencies]]:
    circuit_service = _create_circuit_service()

    def fn() -> Iterator[Dependencies]:
        session = SessionLocal()
        try:
            yield Dependencies(
                session=session,
                get_circuit_use_case=circuit_service,
            )
        finally:
            session.close()

    return fn


get_dependencies = _create_dependencies()
