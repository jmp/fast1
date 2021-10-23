from sqlalchemy.engine import Engine


def check_health(engine: Engine) -> None:
    with engine.connect() as connection:
        connection.execute("SELECT 1;")
