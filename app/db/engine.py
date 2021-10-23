from sqlalchemy import engine


def create_engine(database_url: str) -> engine.Engine:
    return engine.create_engine(database_url)
