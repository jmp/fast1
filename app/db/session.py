from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker


def create_session(engine: Engine) -> Session:
    session = sessionmaker()
    session.configure(bind=engine)  # type: ignore
    return Session()
