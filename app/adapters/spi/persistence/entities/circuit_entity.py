from decimal import Decimal

from sqlalchemy import Column, Float, Integer, String

from app.domain.circuit import Circuit

from .entity import Entity


class CircuitEntity(Entity):
    __tablename__ = "circuits"

    circuit_id = Column("circuitId", Integer, primary_key=True)
    circuit_ref = Column("circuitRef", String, nullable=False)
    name = Column("name", String, nullable=False)
    location = Column("location", String)
    country = Column("country", String)
    lat = Column("lat", Float)
    lng = Column("lng", Float)
    alt = Column("alt", Integer)
    url = Column("url", String, nullable=False)

    def to_domain_model(self) -> Circuit:
        return Circuit(
            id=self.circuit_id or 0,
            ref=str(self.circuit_ref),
            name=str(self.name),
            location=str(self.location),
            country=str(self.country),
            latitude=Decimal(str(self.lat)),
            longitude=Decimal(str(self.lng)),
            altitude=self.alt,
            url=str(self.url),
        )
