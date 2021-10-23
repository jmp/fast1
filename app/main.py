from fastapi import FastAPI

from .api import health, readiness

app = FastAPI()
app.include_router(health.router)
app.include_router(readiness.router)
