import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from tree import *

import os

from config import *

import json_func

import files

import schedule_func

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
    url = getUrl(code)

    try:
        schedule = json_func.downloadJson(url)

        filename = 'schedule-' + code + '.json'

        path = schedulesFilePath

        path += '/' + filename

        files.saveFile(schedule, path)

        return schedule

    except:
        print('Error while downloading schedule ' + code)

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

def setLink(group, subject, link):
    groupCode = getCode(group)

    schedule_func.setLink(groupCode, subject, link)