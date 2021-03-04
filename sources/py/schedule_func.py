import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from datetime import datetime #Узнаем текущее время

import config

schedule_1   = {}
schedule_2   = {}
all_subjects = {}

def load():
    global schedule_1
    global schedule_2 
    global all_subjects

    with codecs.open(config.scheduleFilePath['1'], encoding='utf-8') as schedule1_file:
        #Сохраняем расписание в виде словаря Python
        schedule_1 = json.loads(schedule1_file.read())

    with codecs.open(config.scheduleFilePath['2'], encoding='utf-8') as schedule2_file:
        #Сохраняем расписание в виде словаря Python
        schedule_2 = json.loads(schedule2_file.read())

    with codecs.open(config.subjectsFilePath, encoding='utf-8') as subjects_file:
        #Сохранем пары преподаватель-ссылка в виде словаря Python
        all_subjects = json.loads(subjects_file.read())

'''
with codecs.open(config.scheduleFilePath['1'], encoding='utf-8') as schedule_file:
    #Сохраняем расписание в виде словаря Python
    schedule_1 = json.loads(schedule_file.read())
    
with codecs.open(config.scheduleFilePath['2'], encoding='utf-8') as schedule_file:
    #Сохраняем расписание в виде словаря Python
    schedule_2 = json.loads(schedule_file.read())

with codecs.open(config.subjectsFilePath, encoding='utf-8') as subjects_file:
    #Сохранем пары преподаватель-ссылка в виде словаря Python
    all_subjects = json.loads(subjects_file.read())
'''

''' ---------ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ----------- '''

#Возвращает следующий день. (надо сделать проверку на 30 день)
#Баг с числом

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
    return createDate(2, date_arr)

#Возвращает текушию дату в нужном для сравнения формате
def get_current_date():
    date = str(datetime.now().date()).split('-')
    date.reverse()
    date =  str(date[0]) + '.' + str(date[1]) + '.' + str(date[2])
    print(date)

    return date

#Возвращает текущие время в нужном для сравнения формате
def get_current_time():
    time = str(datetime.now().time()).split(':')
    time =  int(time[0])*60 + int(time[1])
    return time

#Принимает навзание предмета и возвращает ссылку на пару
def url_of_subject(name):
    return all_subjects[name]

#Возвращает дату и время переданного ей предмета
def get_int_time(time):
    time = time[5:]
    time_int = time.split(':')
    time_int = int(time_int[0])*60 + int(time_int[1])
    return time_int


def set_schedule(id):
    if id == '1':
        return schedule_1
    else:
        return schedule_2

def sort_list(list):
    for i in range(0, len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i]['date'] == list[j]['date'] and list[i]['time_int'] < list[j]['time_int']:
                tmp = list[i]
                list[i] = list[j]
                list[j] = tmp

def get_subj_list(id):
    #Список с описанием всех предметов
    list_of_subjects = []
    #
    schedule = set_schedule(id)
    #Для каждого предмета создаем словарь
    for subject in schedule:
        name = subject['ABBR_DISC'] + ' (' + subject['NAME_STUD'] + ')'
        time = subject['TIME_PAIR']
        #Записываем все значения
        dict_of_subject = {}
        dict_of_subject['date']     = subject['DATE_REG']

        if subject['ABBR_DISC'] == '':
            dict_of_subject['name'] = subject['NAME_STUD']
        else:
            dict_of_subject['name'] = subject['ABBR_DISC'] + ' (' + subject['NAME_STUD'] + ')'
        
        dict_of_subject['name'] += ' ' + subject['REASON'] + ' ' + subject['NAME_AUD']

        dict_of_subject['time']     = time
        dict_of_subject['time_int'] = get_int_time(time)
        #dict_of_subject['url']      = url_of_subject(name)

        dict_of_subject['teacher']  = subject['NAME_FIO']
        #Добавляем в список
        list_of_subjects.append(dict_of_subject)

    sort_list(list_of_subjects)

    return list_of_subjects

''' ---------ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ----------- ''' 
