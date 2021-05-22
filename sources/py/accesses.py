import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from tree import *

import os

accesses    = {}
defAccesses = {}

def loadDef(defAccessesFilePath):
    global defAccesses

    with codecs.open(defAccessesFilePath, encoding='utf-8') as defAccesses_file:
        defAccesses = json.loads(defAccesses_file.read())

def load(accessesFilePath):
    global accesses

    with codecs.open(accessesFilePath, encoding='utf-8') as accesses_file:
        accesses = json.loads(accesses_file.read())

def create():
    global accesses

    accesses = defAccesses
   
def save(accessesFilePath):
    with codecs.open(accessesFilePath, "w", encoding='utf-8') as accesses_file:
        json.dump(accesses, accesses_file)

def check(access):
    if accesses.get(access) == None:
        return False
    return True

def add(access, command):
    if check(access) and not accesses[access].count(command):
        accesses[access].append(command)
        return True
    return False

def remove(access, command):
    if check(access) and accesses[access].count(command) > 0:
        accesses[access].remove(command)
        return True
    else:
        return False

def getCommands(access):

    if check(access):
        result = f'In access level {access} available commands:'

        for command in accesses[access]:
            result += f'\n\t{command}'

    else:
        result = f'There is no {access} level of access\n'

    return result

def checkCommand(access, command):
    if check(access) and accesses[access].count(command) > 0:
        return True
    else:
        return False

load(accessesFilePath)