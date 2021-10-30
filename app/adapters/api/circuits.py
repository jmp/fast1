from fastapi import APIRouter, Depends, HTTPException

from app.adapters.api.dependencies import Dependencies, get_dependencies
from app.adapters.api.dtos.circuit_dto import CircuitDto
from app.adapters.api.responses import common_responses
from app.adapters.spi.session import db_session

router = APIRouter(prefix="/circuits")


@router.get(
    "/{ref}",
    response_model=CircuitDto,
    responses=common_responses,
)
async def circuits(
    ref: str, dependencies: Dependencies = Depends(get_dependencies)
) -> CircuitDto:
    db_session.set(dependencies.session)
    use_case = dependencies.get_circuit_use_case
    circuit = use_case.get_circuit(ref)
    if circuit is not None:
        return CircuitDto.from_domain_model(circuit)
    raise HTTPException(404)
