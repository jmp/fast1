from fastapi import FastAPI

from app.adapters.api import health, readiness

app = FastAPI()
app.include_router(health.router)
app.include_router(readiness.router)
