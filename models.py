from pydantic import BaseModel
from pydantic.class_validators import List


class Message(BaseModel):
    channel: str
    text: str


class Body(BaseModel):
    bot_token: str
    channels: List[Message]


class BodyResponse(BaseModel):
    channels: List[Message]
