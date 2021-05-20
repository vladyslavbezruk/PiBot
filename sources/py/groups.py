import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from tree import *

import os

from config import *

import json_func

import files

from time import sleep

groups = files.loadFile(groupsFilePath)

def getUrl(code):
    return site + code

def getCode(name):
    for group in groups.keys():
        if group.lower() == name.lower():
            return groups[group]
    return -1

def getName(code):
    for group in groups.keys():
        if groups[group].lower() == code.lower():
            return group

def getSchedule(code):
#    print(code)

    url = getUrl(code)

    schedule = json_func.downloadJson(url)

    filename = 'schedule-' + code + '.json'

    path = schedulesFilePath

    path += '/' + filename

    #print(path)

    files.saveFile(schedule, path)

    return schedule

def update():
    flag = 0
    result = 'Оновлено розклад для: '

    for group in groups.keys():
        code = groups[group]
        filename = 'schedule-' + code + '.json'
        path = schedulesFilePath + '/' + filename

        if os.path.exists(path) == True:
            flag = 1
            getSchedule(code)

            result += f'{group} '
            print(f'Updated {code}')
    if flag:
        return result
    else:
        return 'Не було оновлено розклад'

'''
for group in groups.keys():
    code = groups[group]

    #sleep(0.1)

    getSchedule(code)

print("Done!")
'''
