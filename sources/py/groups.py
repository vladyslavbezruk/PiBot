import sources.py.files as files
import sources.py.json_func as json_func
import sources.py.schedule_func as schedule_func
from sources.py.config import *
from sources.py.tree import *

groups = files.loadFile(groupsFilePath)

def getUrl(code):
    return site + code

def getCode(name):
    for code in groups.keys():
        if groups[code].lower() == name.lower():
            return code
    return -1

def getName(group_code):
    for code in groups.keys():
        if code == group_code:
            return groups[code]

def checkGroup(name):
    for code in groups.keys():
        if groups[code].lower() == name.lower():
            return True
    return False

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

def updateGroups():
    try:
        global groups

        path = groupsFilePath

        files.saveFile(json_func.downloadJson(site_groups), path)

        groups = files.loadFile(groupsFilePath)
 
        print('Оновлено групи')
    except:
        print('Не було оновлено групи')

def update():
    updateGroups()
    
    flag = 0
    result = 'Оновлено розклад для: '

    for code in groups.keys():
        group = groups[code]
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
