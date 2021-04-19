import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from config import *

chats = {}

def load(chatsFilePath):
    global chats

    with codecs.open(chatsFilePath, encoding = 'utf-8') as chats_file:
        chats = json.loads(chats_file.read())

    return chats

def save(chatsFilePath):
    with codecs.open(chatsFilePath, "w", encoding = 'utf-8') as chats_file:
        json.dump(chats, chats_file)

def create(id):
    chat = {}

    chat[id] = []

def addChat(chat_id):
    #chats.append(create(id))

    chats[chat_id] = []

    save(chatsFilePath)

def checkChat(chat_id):
    for key in chats.keys():
        if chat_id == key:
            return True
    return False

def findChat(chat_id):
    i = 0

    for key in chats.keys():
        if chat_id == key:
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
