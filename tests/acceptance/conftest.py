from sqlalchemy.exc import OperationalError

from app.adapters.spi.session import SessionLocal


def no_database() -> bool:
    try:
        with SessionLocal().bind.connect():  # type: ignore
            return False
    except (OperationalError, AttributeError):
        return True
