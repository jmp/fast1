from typing import Any

from app.adapters.api.dtos.message_dto import MessageDto

common_responses: dict[int | str, dict[str, Any]] = {
    404: {
        "model": MessageDto,
        "description": "The item was not found.",
        "content": {"application/json": {"example": {"detail": "Not Found"}}},
    },
}
