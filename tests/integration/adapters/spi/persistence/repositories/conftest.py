from decimal import Decimal
from typing import Iterator

from _pytest.fixtures import fixture
from sqlalchemy.orm import Session

from app.adapters.spi.persistence.entities.circuit_entity import CircuitEntity
from app.adapters.spi.persistence.entities.entity import Entity
from app.adapters.spi.persistence.session import SessionLocal, engine


@fixture(scope="session")
def session() -> Iterator[Session]:
    Entity.metadata.create_all(bind=engine)
    session = SessionLocal()
    entity = CircuitEntity(
        circuit_id=14,
        circuit_ref="monza",
        name="Autodromo Nazionale di Monza",
        location="Monza",
        country="Italy",
        lat=Decimal("45.6156"),
        lng=Decimal("9.28111"),
        alt=162,
        url="http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza",
    )
    session.add(entity)
    session.commit()
    yield session
    session.close()
    Entity.metadata.drop_all(bind=engine)
