import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

import os

import accesses

usersFilePath = os.path.join("..", "..", "resources", "json", "users.json")

users = {}

def load(usersFilePath):
    global users

    with codecs.open(usersFilePath, encoding='utf-8') as users_file:
        users = json.loads(users_file.read())

def create():

    global users

    users = {}
    
    users['admin'] = []
    users['user'] = []
     
    #userspath = os.path.join("..", "..", "resources", "json", usersFile)
    #userspath = os.path.join(usersFile)
   
def save(usersFilePath):
    with codecs.open(usersFilePath, "w", encoding='utf-8') as users_file:
        json.dump(users, users_file)
        
def checkUser(access, t_id):
    if users.get(access) == None:
        return False
    
    for user in users[access]:
        if user['id'] == t_id:
            return True
    return False
    
def addUser(access, t_id, group):
    user = {}
    user['id'] = t_id
    user['group'] = group
    users[access].append(user)

create()
addUser('admin', 123, 'IN-01')
save(usersFilePath)
accesses.save(accesses.accessesFilePath)
