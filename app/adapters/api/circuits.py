from fastapi import APIRouter, Depends, HTTPException

from app.adapters.api.dtos.circuit_dto import CircuitDto
from app.dependencies import Dependencies, get_dependencies

router = APIRouter()


@router.get("/circuits/{ref}", response_model=CircuitDto)
async def circuits(
    ref: str, dependencies: Dependencies = Depends(get_dependencies)
) -> CircuitDto:
    use_case = dependencies.get_circuit_use_case
    circuit = use_case.get_circuit(ref)
    if circuit is not None:
        return CircuitDto.from_domain_model(circuit)
    raise HTTPException(404)
