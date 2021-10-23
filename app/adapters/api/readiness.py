from fastapi import APIRouter

router = APIRouter()


@router.get("/readiness")
async def readiness() -> None:
    pass
