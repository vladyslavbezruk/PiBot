from config import *
from tree import *

import json_func

from aiogram.types import Message

def push(message: Message):
    global messages

    messages = json_func.loadJson(messagesFilePath)

    text = f"username = @{message.from_user.username} name = {message.from_user.first_name} chat_id = {message.chat.id} user_id = {message.from_user.id}\nMessage: {message.text}"

    messages.append(text)

    json_func.saveJson(messages, messagesFilePath)