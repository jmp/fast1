from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Circuit:
    id: int
    ref: str
    name: str
    location: Optional[str]
    country: Optional[str]
    latitude: Optional[Decimal]
    longitude: Optional[Decimal]
    altitude: Optional[float]
    url: str
