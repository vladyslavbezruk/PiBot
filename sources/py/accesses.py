import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

import files

from tree import *

import os

accesses    = {}
defAccesses = {}

def load(accessesFilePath):
    global accesses

    accesses = files.loadFile(accessesFilePath)

def create():
    global accesses

    accesses = defAccesses
   
def save(accessesFilePath):
    files.saveFile(accesses, accessesFilePath)

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
        result = f'У вас рівень {access}. Ви маєте такі команди:'

        for command in accesses[access]:
            result += f'\n\t{command}'

    else:
        result = f'Немає команд для рівня {access}\n'

    return result

def checkCommand(access, command):
    if check(access) and accesses[access].count(command) > 0:
        return True
    else:
        return False

load(accessesFilePath)