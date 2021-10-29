from contextvars import ContextVar
from os import environ
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

_engine = create_engine(
    environ.get("DATABASE_URL", "mariadb+mariadbconnector://db:db@127.0.0.1:3306/db"),
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


db_session: ContextVar[Optional[Session]] = ContextVar("db_session", default=None)
