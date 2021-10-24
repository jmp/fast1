from dataclasses import dataclass


@dataclass
class Circuit:
    id: int
    ref: str
    name: str
    location: str
    country: str
    latitude: float
    longitude: float
    altitude: float
    url: str
