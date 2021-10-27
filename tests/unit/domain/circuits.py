from decimal import Decimal

from app.domain.circuit import Circuit

monza = Circuit(
    id=14,
    ref="monza",
    name="Autodromo Nazionale di Monza",
    location="Monza",
    country="Italy",
    latitude=Decimal("45.6156"),
    longitude=Decimal("9.28111"),
    altitude=162,
    url="http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza",
)
