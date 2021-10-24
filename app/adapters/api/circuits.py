from typing import Any

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/circuits/{ref}")
async def circuits(ref: str) -> dict[str, Any]:
    if ref == "monza":
        return {
            "ref": "monza",
            "name": "Autodromo Nazionale di Monza",
            "location": "Monza",
            "country": "Italy",
            "latitude": 45.6156,
            "longitude": 9.28111,
            "altitude": 162,
            "url": "http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza",
        }
    raise HTTPException(404)
