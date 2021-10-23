from fastapi import APIRouter

from ..db.engine import engine
from ..health import check_health

router = APIRouter()


@router.get("/health")
async def health() -> dict[str, str]:
    check_health(engine)
    return {"status": "OK"}
