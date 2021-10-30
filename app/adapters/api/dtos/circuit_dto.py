from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from app.domain.circuit import Circuit


class CircuitDto(BaseModel):
    ref: str
    name: str
    location: Optional[str]
    country: Optional[str]
    latitude: Optional[Decimal]
    longitude: Optional[Decimal]
    altitude: Optional[float]
    url: str

    class Config:
        frozen = True
        title = "Circuit"
        schema_extra = {
            "example": {
                "ref": "spa",
                "name": "Circuit de Spa-Francorchamps",
                "location": "Spa",
                "country": "Belgium",
                "latitude": 50.437198638916016,
                "longitude": 5.9713897705078125,
                "altitude": 401.0,
                "url": "http://en.wikipedia.org/wiki/Circuit_de_Spa-Francorchamps",
            }
        }

    @staticmethod
    def from_domain_model(circuit: Circuit) -> "CircuitDto":
        return CircuitDto(
            ref=circuit.ref,
            name=circuit.name,
            location=circuit.location,
            country=circuit.country,
            latitude=circuit.latitude,
            longitude=circuit.longitude,
            altitude=circuit.altitude,
            url=circuit.url,
        )
