from pydantic import BaseModel


class MessageDto(BaseModel):
    detail: str

    class Config:
        frozen = True
        title = "Message"
