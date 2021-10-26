from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from app.domain.circuit import Circuit


class CircuitDto(BaseModel):
    name: str
    location: Optional[str]
    country: Optional[str]
    latitude: Optional[Decimal]
    longitude: Optional[Decimal]
    altitude: Optional[float]
    url: str

    @staticmethod
    def from_domain_model(circuit: Circuit) -> "CircuitDto":
        return CircuitDto(
            name=circuit.name,
            location=circuit.location,
            country=circuit.country,
            latitude=circuit.latitude,
            longitude=circuit.longitude,
            altitude=circuit.altitude,
            url=circuit.url,
        )
