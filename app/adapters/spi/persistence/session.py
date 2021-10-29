from contextvars import ContextVar
from os import environ
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine(
    environ.get("DATABASE_URL", "mariadb+mariadbconnector://db:db@127.0.0.1:3306/db"),
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


db_session: ContextVar[Optional[Session]] = ContextVar("db_session", default=None)
