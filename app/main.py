from fastapi import FastAPI

from .adapters.api import circuits

app = FastAPI()
app.include_router(circuits.router)
