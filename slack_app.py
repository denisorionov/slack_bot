import json
import logging

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logger = logging.getLogger(__name__)


def send_messages(messages):
    try:
        messages = json.loads(messages)
        client = WebClient(token=messages["bot_token"])

        for message in messages["channels"]:
            client.chat_postMessage(
                channel=message["channel"],
                text=message["text"]
            )

        return

    except SlackApiError as e:
        print(f"Error: {e}")
