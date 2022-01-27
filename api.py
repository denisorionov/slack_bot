from fastapi import FastAPI

from models import Body, BodyResponse
from slack_app import send_messages

app = FastAPI()


@app.post("/message/", response_model=BodyResponse)
async def create_item(message: Body):
    send_messages(message.json())
    return message
