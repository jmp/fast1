from contextvars import ContextVar
from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

_engine = create_engine(
    environ.get("DATABASE_URL", "mariadb+mariadbconnector://db:db@127.0.0.1:3306/db"),
    connect_args={"connect_timeout": 10},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


db_session: ContextVar[Session] = ContextVar("db_session")
