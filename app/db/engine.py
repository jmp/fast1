from sqlalchemy.engine import Engine
from sqlalchemy.engine import create_engine as _create_engine

from ..settings import settings


def create_engine(database_url: str) -> Engine:
    return _create_engine(database_url)


engine = create_engine(settings.database_url)
