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
            ref=self.circuit_ref or "",
            name=self.name or "",
            location=self.location,
            country=self.country,
            latitude=Decimal(str(self.lat)) if self.lat is not None else None,
            longitude=Decimal(str(self.lng)) if self.lng is not None else None,
            altitude=self.alt,
            url=self.url or "",
        )
