from fastapi import FastAPI

from .api import health

app = FastAPI()
app.include_router(health.router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"msg": "Hello World"}
