from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import Dependencies, get_dependencies

router = APIRouter()


@router.get("/circuits/{ref}")
async def circuits(
    ref: str, dependencies: Dependencies = Depends(get_dependencies)
) -> dict[str, Any]:
    circuit_service = dependencies.circuit_service
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
