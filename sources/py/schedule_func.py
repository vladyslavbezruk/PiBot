import json_func

import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from datetime import datetime #Узнаем текущее время

''' Читаем с .json список предметов и словарь преподователь-ссылка '''
'''
with codecs.open("../../resources/json/schedule1.json", encoding='utf-8') as schedule_file:
    #Сохраняем расписание в виде словаря Python
    schedule = json.loads(schedule_file.read())

with codecs.open("../../resources/json/subjects.json", encoding='utf-8') as subjects_file:
    #Сохранем пары преподаватель-ссылка в виде словаря Python
    all_subjects = json.loads(subjects_file.read())
'''
''' Читаем с .json список предметов и словарь преподователь-ссылка '''

''' ---------ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ----------- '''

with codecs.open("schedule1.json", encoding='utf-8') as schedule_file:
    #Сохраняем расписание в виде словаря Python
    schedule = json.loads(schedule_file.read())

with codecs.open("subjects.json", encoding='utf-8') as subjects_file:
    #Сохранем пары преподаватель-ссылка в виде словаря Python
    all_subjects = json.loads(subjects_file.read())
    
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
def url_of_subject(subj_name):
    return all_subjects.get(subj_name)

#Возвращает дату и время переданного ей предмета
def get_date_and_time(subj):
    
    description = subj['VALARM'][0]['DESCRIPTION'].split()
    #первое появление числа - дата, потом - время
    flag = False
    
    for element in description:
        if element[0].isdigit() and flag == False:
            date = element
            flag = True
        elif element[0].isdigit() and flag:
            time = element
            time_int = element.split(':')
            time_int = int(time_int[0])*60 + int(time_int[1])
            break
    return (date, time_int, time)

#Возвращает имя преподователя для строки DESCRIPTION
def get_teacher_name(description):
    return description.split('\\')[0]

''' ---------ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ----------- '''

#Список с описанием всех предметов
list_of_subjects = []
#Для каждого предмета создаем словарь
for subject in schedule['VCALENDAR'][0]['VEVENT']:
    dict_of_subject = {}
    #Сохраняем название предмета
    subj_name = subject['SUMMARY']
    #Идем в функцию и забираем дату и время. 0 - дата, 1 - врямя для сравнения, 2 - время в виде строки
    date_time = get_date_and_time(subject)
    #Записываем все значения
    dict_of_subject['name']     = subj_name
    dict_of_subject['date']     = date_time[0]
    dict_of_subject['time_int'] = date_time[1]
    dict_of_subject['time']     = date_time[2]
    dict_of_subject['url']      = url_of_subject(subj_name)
    dict_of_subject['teacher']  = get_teacher_name(subject['DESCRIPTION'])
    #Добавляем в список
    list_of_subjects.append(dict_of_subject)

#Возвращает следующий день. (надо сделать проверку на 30 день)
#
def date_tomorrow(date):
    date_arr = date.split('.')
    today = int(date_arr[0])
    today += 1
    date = str(today) + '.' + date_arr[1] + '.' + date_arr[2]
    return date
