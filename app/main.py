from fastapi import FastAPI

from .db.engine import create_engine
from .health import check_health
from .settings import Settings

settings = Settings()
engine = create_engine(settings.database_url)
app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"msg": "Hello World"}


@app.get("/health")
def health() -> dict[str, str]:
    check_health(engine)
    return {}
