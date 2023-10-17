import sources.py.files as files
import sources.py.logs as logs
from sources.py.tree import *

chats = {}


def load(chatsFilePath):
    global chats

    chats = files.loadFile(chatsFilePath)

    return chats


def save(chatsFilePath):
    files.saveFile(chats, chatsFilePath)


def create(id):
    chat = {}

    chat[id] = []


def addChat(chat_id):
    logs.writeLog(f'Aded new chat with id {chat_id}')

    chats[chat_id] = []

    save(chatsFilePath)


def checkChat(chat_id):
    for key in chats.keys():
        if str(chat_id) == str(key):
            return True
    return False


def findChat(chat_id):
    i = 0

    for key in chats.keys():
        if str(chat_id) == str(key):
            return i
        i = i + 1
    return -1


def removeChat(chat_id):
    i = findChat(chat_id)

    if i != -1:
        chats.pop(i)

    save(chatsFilePath)


def checkGroup(chat_id, group):
    if checkChat(chat_id) == True:
        if group in chats[chat_id]:
            return True
    return False


def addGroup(chat_id, group):
    if checkChat(chat_id) == False:
        addChat(chat_id)

    if checkGroup(chat_id, group) == False:
        chats[chat_id].append(group)

    save(chatsFilePath)


def removeGroup(chat_id, group):
    if checkChat(chat_id) == False:
        addChat(chat_id)

    if checkGroup(chat_id, group) == True:
        chats[chat_id].remove(group)

    save(chatsFilePath)


load(chatsFilePath)
