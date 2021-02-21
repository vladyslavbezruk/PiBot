import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

import os

accessesFile = 'accesses.json'

defAccessesFile = 'defAccesses.json'

accesses = {}
defAccesses = {}

def loadDef(defAccessesFile):
    global defAccesses
    with codecs.open("defAccesses.json", encoding='utf-8') as defAccesses_file:
        defAccesses = json.loads(defAccesses_file.read())

def load(accessesFile):
    global accesses

    with codecs.open("accesses.json", encoding='utf-8') as accesses_file:
        accesses = json.loads(accesses_file.read())

def create():
    global accesses

    accesses = defAccesses
   
def save(accessesFile):
    with codecs.open("accesses.json", "w", encoding='utf-8') as accesses_file:
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

def checkCommand(access, command):
    if check(access) and accesses[access].count(command) > 0:
        return True
    else:
        return False

'''
print(add('admin1', '/set'))
print(add('admin', '/set1'))
print(add('admin', '/set2'))
print(remove('admin', '/update'))
print(remove('admin', '/update'))

print(checkCommand('admin', '/getJson'))
print(checkCommand('admin', '/update'))
'''

#save(accessesFile)

loadDef(defAccessesFile)
create()