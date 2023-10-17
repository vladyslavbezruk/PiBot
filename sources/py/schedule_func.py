from datetime import datetime
import sources.py.files as files
import sources.py.groups as groups
from sources.py.tree import *

schedules = {}

all_subjects = {}

def load():
    global schedules
    global all_subjects

    schedules = {}

    for code in groups.groups.keys():
        group = groups.groups[code]
        
        filename = 'schedule-' + code + '.json'
        path = schedulesFilePath + '/' + filename

        if os.path.exists(path) == True:
            schedule = files.loadFile(path)

            schedules[code] = schedule

    all_subjects = files.loadFile(subjectsFilePath)

def getLength(num):
    length = 1
    num = int(num)

    while num >= 10:
        length = length + 1
        num = num / 10

    return length

def getStrFormat(format, num):
    length = getLength(int(num))
    bkp = str(int(num))
    cNum = ''

    if length < format:
        for i in range(format - length):
            cNum += '0'

    cNum += bkp

    return cNum

def createDate(format, date):
    cDate = getStrFormat(format, date[0])

    flag = 0

    for num in date:
        if flag == 1:
            cDate += '.' + getStrFormat(format, num)
        flag = 1

    return cDate


def date_tomorrow(date):
    date_arr = date.split('.')
    date_arr[0] = str(int(date_arr[0]) + 1)
    
    if int(date_arr[0]) > 31 and date_arr[1] == '1':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
        
    if int(date_arr[0]) > 28 and date_arr[1] == '2':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
    
    if int(date_arr[0]) > 31 and date_arr[1] == '3':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
        
    if int(date_arr[0]) > 30 and date_arr[1] == '4':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
    
    if int(date_arr[0]) > 31 and date_arr[1] == '5':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
    
    if int(date_arr[0]) > 30 and date_arr[1] == '6':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
    
    if int(date_arr[0]) > 31 and date_arr[1] == '7':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
    
    if int(date_arr[0]) > 31 and date_arr[1] == '8':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
    
    if int(date_arr[0]) > 30 and date_arr[1] == '9':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
    
    if int(date_arr[0]) > 31 and date_arr[1] == '10':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
    
    if int(date_arr[0]) > 30 and date_arr[1] == '11':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
    
    if int(date_arr[0]) > 31 and date_arr[1] == '12':
        date_arr[0] = '1'
        date_arr[1] = str(int(date_arr[1]) + 1)
    
    if int(date_arr[1]) > 12:
        date_arr[1] = '1'
        date_arr[2] = str(int(date_arr[2]) + 1)

    return createDate(2, date_arr)

def get_current_date():
    date = str(datetime.now().date()).split('-')
    date.reverse()
    date = str(date[0]) + '.' + str(date[1]) + '.' + str(date[2])

    return date

def get_current_time():
    time = str(datetime.now().time()).split(':')
    time = int(time[0]) * 60 + int(time[1])
    return time

def url_of_subject(id, namea, nameb):
    name = namea + ' (' + nameb + ')'
    if id not in all_subjects.keys():
        return 'Немає посилання на заняття'

    if name in all_subjects[id].keys():
        return all_subjects[id][name]

    return 'Немає посилання на заняття'

def get_int_time(time):
    time_int = time.split(':')
    time_int = int(time_int[0]) * 60 + int(time_int[1])
    return time_int

def set_schedule(id):
    code = id
    filename = 'schedule-' + code + '.json'
    path = schedulesFilePath + '/' + filename

    if os.path.exists(path) == False:
        groups.getSchedule(code)
        load()

    return schedules[code]

def sort_list(list):
    for i in range(0, len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i]['date'] == list[j]['date'] and get_int_time(list[i]['time_begin']) > get_int_time(
                    list[j]['time_begin']):
                tmp = list[i]
                list[i] = list[j]
                list[j] = tmp

def get_subj_list(id):
    list_of_subjects = []
    
    schedule = set_schedule(id)

    for subject in schedule:
        name = subject['ABBR_DISC'] + ' (' + subject['NAME_STUD'] + ')'
        time = subject['TIME_PAIR']
        
        dict_of_subject = {}
        dict_of_subject['date'] = subject['DATE_REG']

        if subject['ABBR_DISC'] == '':
            dict_of_subject['name'] = subject['NAME_STUD']
        else:
            dict_of_subject['name'] = subject['ABBR_DISC'] + ' (' + subject['NAME_STUD'] + ')'

        dict_of_subject['name'] += ' ' + subject['REASON'] + ' ' + subject['NAME_AUD']

        dict_of_subject['time_begin'] = time[0:5]
        dict_of_subject['time_end'] = time[6:]

        dict_of_subject['url'] = url_of_subject(id, subject['ABBR_DISC'], subject['NAME_STUD'])

        dict_of_subject['teacher'] = subject['NAME_FIO']

        list_of_subjects.append(dict_of_subject)

    sort_list(list_of_subjects)

    return list_of_subjects

def setLink(code, subject, link):
    if all_subjects.get(code) == None:
        all_subjects[code] = {}

    all_subjects[code][subject] = link

    files.saveFile(all_subjects, subjectsFilePath)