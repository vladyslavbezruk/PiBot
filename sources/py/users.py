import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

import logs

import os

import accesses

import files

from config import *

from tree import *

users = {}

def load(usersFilePath):
    global users

    users = files.loadFile(usersFilePath)

    return users

def create():

    global users

    users = {}
    
    users['admin'] = []
    users['user'] = []
   
def save(usersFilePath):
    files.saveFile(users, usersFilePath)
        
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

    save(usersFilePath)

    logs.writeLog(f'Aded new user with id {t_id}')

def searchUser(access, t_id):
    i = 0
    for user in users[access]:
        if user['id'] == t_id:
            return i
        i = i + 1

def checkUser(t_id):
    access = getAccess(t_id)
    
    if access == None:
        return False
    else:
        return True
    
def set(access, t_id, setting, value):
    if checkUser(t_id):
        users[access][searchUser(access, t_id)][setting] = value

def get(access, t_id, setting):
    if checkUser(t_id):
        return users[access][searchUser(access, t_id)][setting]

def getAccess(t_id):
    for access in users.keys():
        for user in users[access]:
            if user['id'] == t_id:
                return access
    return None
    
def checkCommand(t_id, command):
    return accesses.checkCommand(getAccess(t_id), command)
                
load(usersFilePath)
