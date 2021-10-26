from fastapi import APIRouter, Depends, HTTPException

from app.adapters.api.dtos.circuit_dto import CircuitDto
from app.dependencies import Dependencies, get_dependencies

router = APIRouter()


@router.get("/circuits/{ref}", response_model=CircuitDto)
async def circuits(
    ref: str, dependencies: Dependencies = Depends(get_dependencies)
) -> CircuitDto:
    circuit_service = dependencies.circuit_service
    circuit = circuit_service.get_circuit(ref)
    if circuit is not None:
        return CircuitDto.from_domain_model(circuit)
    raise HTTPException(404)
