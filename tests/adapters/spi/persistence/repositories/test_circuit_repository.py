from app.adapters.spi.persistence.entities.circuit_entity import CircuitEntity
from app.adapters.spi.persistence.repositories.circuit_repository import (
    CircuitRepository,
)


def test_get_circuit_returns_entity_if_it_exists() -> None:
    repository = CircuitRepository()
    expected = CircuitEntity(
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
    entity = repository.get_circuit("monza")
    assert entity is not None
    assert entity.circuit_id == expected.circuit_id
    assert entity.circuit_ref == expected.circuit_ref
    assert entity.name == expected.name
    assert entity.location == expected.location
    assert entity.country == expected.country
    assert entity.lat == expected.lat
    assert entity.lng == expected.lng
    assert entity.alt == expected.alt
    assert entity.url == expected.url


def test_get_circuit_returns_none_if_it_does_not_exist() -> None:
    repository = CircuitRepository()
    entity = repository.get_circuit("does_not_exist")
    assert entity is None
