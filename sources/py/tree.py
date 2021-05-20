import os

import asyncio

accessesFilePath = os.path.join("..", "..", "resources", "json", "accesses.json")
defAccessesFilePath = os.path.join("..", "..", "resources", "json", "defAccesses.json")

createSource = "../sh/createSource.sh"

removeSource = "../sh/removeSource.sh"

gitPush = "../sh/git-push.sh"

schedulesFilePath = os.path.join("..", "..", "resources", "json", "schedules")

scheduleFilePath = {}
scheduleFilePath['1'] = os.path.join("..", "..", "resources", "json", "schedule_1.json")
scheduleFilePath['2'] = os.path.join("..", "..", "resources", "json", "schedule_2.json")

usersFilePath = os.path.join("..", "..", "resources", "json", "users.json")

groupsFilePath = os.path.join("..", "..", "resources", "json", "groups.json")

subjectsFilePath = os.path.join("..", "..", "resources", "json", "subjects.json")

chatsFilePath = os.path.join("..", "..", "resources", "json", "chats.json")

messagesFilePath = os.path.join("..", "..", "resources", "json", "messages.json")
