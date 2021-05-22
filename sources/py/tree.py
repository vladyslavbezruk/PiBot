import os

import asyncio

accessesFilePath = os.path.join("..", "..", "resources", "json", "accesses.json")
defAccessesFilePath = os.path.join("..", "..", "resources", "json", "defAccesses.json")

createSource = "../sh/createSource.sh"

removeSource = "../sh/removeSource.sh"

schedulesFilePath = os.path.join("..", "..", "resources", "json", "schedules")

scheduleFilePath = {}

usersFilePath = os.path.join("..", "..", "resources", "json", "users.json")

groupsFilePath = os.path.join("..", "..", "resources", "json", "groups.json")

subjectsFilePath = os.path.join("..", "..", "resources", "json", "subjects.json")

chatsFilePath = os.path.join("..", "..", "resources", "json", "chats.json")

messagesFilePath = os.path.join("..", "..", "resources", "json", "messages.json")
