from pytest import fixture

from app.domain.circuit import Circuit


@fixture
def monza() -> Circuit:
    return Circuit(
        id=14,
        ref="monza",
        name="Autodromo Nazionale di Monza",
        location="Monza",
        country="Italy",
        latitude=45.6156,
        longitude=9.28111,
        altitude=162,
        url="http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza",
    )
