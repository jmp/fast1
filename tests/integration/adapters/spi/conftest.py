from decimal import Decimal
from typing import Iterator

from _pytest.fixtures import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.adapters.spi.entities.circuit_entity import CircuitEntity
from app.adapters.spi.entities.entity import Entity
from app.adapters.spi.session import db_session

_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


@fixture(scope="session")
def session() -> Iterator[Session]:
    Entity.metadata.create_all(bind=_engine)
    session = _SessionLocal()
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
    db_session.set(session)
    yield session
    session.close()
    Entity.metadata.drop_all(bind=_engine)
