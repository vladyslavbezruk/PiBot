import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from tree import *

from config import *

import json_func

import files

groups = files.loadFile(groupsFilePath)

def getUrl(code):
    return site + code

def getCode(name):
    for group in groups.keys():
        if group.lower() == name.lower():
            return groups[group]
    return -1

def getSchedule(code):
    print(code)

    url = getUrl(code)

    schedule = json_func.downloadJson(url)

    filename = 'schedule-' + code + '.json'

    path = schedulesFilePath.join(filename)

    files.saveFile(schedule, path)

for group in groups.keys():
    code = groups[group]

    getSchedule(code)


