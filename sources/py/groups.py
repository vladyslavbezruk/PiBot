import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from config import *

from users import load

from datetime import datetime #Узнаем текущее время

def loadGroups(groupsFilePath):
    with codecs.open(groupsFilePath, encoding='utf-8') as groups_file:
        groups = json.loads(groups_file.read())
        
    return groups

def saveGroups(groupsFilePath, groups):
    with codecs.open(groupsFilePat, "w", encoding='utf-8') as groups_file:
        json.dump(groups, groups_file)
        
def updateGroupsList(usersFilePath, groups):
    
    users = load(usersFilePath):
    
    for access in users:
        for user in access:
            if groups.count(user['group']) == 0
                groups.append(user['group'])
                
    return groups
    
def updatingGroupsList(usersFilePath, groupsFilePath):
    saveGroups(groupsFilePath, updateGroupsList(usersFilePath, loadGroups(groupsFilePath)))
