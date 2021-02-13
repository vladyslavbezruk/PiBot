import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from datetime import datetime #Узнаем текущее время
 
with codecs.open('schedule1.json', encoding='utf-8') as schedule_file:
    #Сохраняем расписание в виде словаря Python
    schedule = json.loads(schedule_file.read())

with codecs.open('subjects.json', encoding='utf-8') as subjects_file:
    #Сохранем пары преподаватель-ссылка в виде словаря Python
    subjects = json.loads(subjects_file.read())

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
    return subjects.get(subj_name)

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
            time = element.split(':')
            time = int(time[0])*60 + int(time[1])
            break
    return (date, time)

def help_get_url():
    classes_today = False
    
    date = get_current_date()
    time = get_current_time()
    
    # Инфа об занятиях хранится в массиве shelude['VCALENDAR'][0]['VEVENT']
    # В виде словаря, название предмета в ключе 'SUMMARY'
    for subject in schedule['VCALENDAR'][0]['VEVENT']:
        #Сохраняем название предмета
        subj_name = subject['SUMMARY']
        date_time = get_date_and_time(subject)
        if (date_time[0] == date and time < date_time[1]):
            result = url_of_subject(subj_name)
            classes_today = True
            break
    if classes_today:
        return result
    else:
        return 'Сегодня занятий нет!'
