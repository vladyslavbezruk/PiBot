import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from datetime import datetime #Узнаем текущее время

import config


schedule_1   = {}
schedule_2   = {}
all_subjects = {}

#with codecs.open(scheduleFilePath[str(id)], encoding='utf-8') as schedule_file:
with codecs.open('schedule_1.json', encoding='utf-8') as schedule_file:
    #Сохраняем расписание в виде словаря Python
    schedule_1 = json.loads(schedule_file.read())
    
with codecs.open('schedule_2.json', encoding='utf-8') as schedule_file:
    #Сохраняем расписание в виде словаря Python
    schedule_1 = json.loads(schedule_file.read())

with codecs.open(config.subjectsFilePath, encoding='utf-8') as subjects_file:
    #Сохранем пары преподаватель-ссылка в виде словаря Python
    all_subjects = json.loads(subjects_file.read())
    

''' ---------ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ----------- '''

#Возвращает следующий день. (надо сделать проверку на 30 день)
#Баг с числом
def date_tomorrow(date):
    date_arr = date.split('.')
    today = int(date_arr[0])
    today += 1
    date = str(today) + '.' + date_arr[1] + '.' + date_arr[2]
    return date

#Возвращает текушию дату в нужном для сравнения формате
def get_current_date():
    date = str(datetime.now().date()).split('-')
    date.reverse()
    date =  str(date[0]) + '.' + str(date[1]) + '.' + str(date[2])
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
    if id == 1:
        return schedule_1
    else:
        return schedule_2
        
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
        dict_of_subject['name']     = subject['ABBR_DISC']
        dict_of_subject['date']     = subject['DATE_REG']
        dict_of_subject['time']     = time
        dict_of_subject['time_int'] = get_int_time(time)
        dict_of_subject['url']      = url_of_subject(name)
        dict_of_subject['teacher']  = subject['NAME_FIO']
        #Добавляем в список
        list_of_subjects.append(dict_of_subject)
        
    return list_of_subjects
''' ---------ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ----------- ''' 
