from fastapi import FastAPI

from .api import health

app = FastAPI()
app.include_router(health.router)
