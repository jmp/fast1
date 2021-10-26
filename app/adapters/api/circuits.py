from typing import Any

from fastapi import APIRouter, HTTPException

from app.dependencies import get_dependencies

router = APIRouter()
circuit_service = get_dependencies().circuit_service


@router.get("/circuits/{ref}")
async def circuits(ref: str) -> dict[str, Any]:
    circuit = circuit_service.get_circuit(ref)
    if circuit is None:
        raise HTTPException(404)
    return {
        "ref": circuit.ref,
        "name": circuit.name,
        "location": circuit.location,
        "country": circuit.country,
        "latitude": circuit.latitude,
        "longitude": circuit.longitude,
        "altitude": circuit.altitude,
        "url": circuit.url,
    }
