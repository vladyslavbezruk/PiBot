'''
Модуль для работы с расписанием.

help_get_url()
возвращает словарь с полями subject (имя предмета),
teacher (имя преподователя), url, date, time для ближайшей пары
или None, если такого не нашлось

help_today()
Возвращает строку в которой перечень занятий на сегодня

help_tomorrow()
Возвращает строку в которой перечень занятий на завтра

Все остальные функции - вспомогательные, не трогать!
'''

import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from datetime import datetime #Узнаем текущее время


''' Читаем с .json список предметов и словарь преподователь-ссылка '''
# !!!!!!!!!!!!!!!!!!!!
with codecs.open("../../resources/json/schedule1.json", encoding='utf-8') as schedule_file:
    #Сохраняем расписание в виде словаря Python
    schedule = json.loads(schedule_file.read())

with codecs.open("../../resources/json/subjects.json", encoding='utf-8') as subjects_file:
    #Сохранем пары преподаватель-ссылка в виде словаря Python
    subjects = json.loads(subjects_file.read())
''' Читаем с .json список предметов и словарь преподователь-ссылка '''



    
''' ---------ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ----------- '''

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



''' ---------ОСНОВНЫЕ ФУНКЦИИ----------- '''
#Возвращает словарь с описанием ближайшего занятия или None
def help_get_url():
    
    #Есть ли сегодня занятия, по умолчанию - нет
    classes_today = False

    #Берем текущую дату и время в необходимом для сравнения варианте
    date = get_current_date()
    time = get_current_time()
    
    for subject in list_of_subjects:
        #Если дата текущая и время меньше, чем начало пары
        if (subject['date'] == date and time < subject['time_int']):
            classes_today = True
            break
    if classes_today:
        return {'subject': subject['name'], 'teacher': subject['teacher'], 'url': subject['url'],
                'date': subject['date'], 'time': subject['time']}
    else:
        return None

def help_today():
    #Есть ли сегодня занятия, по умолчанию - нет
    classes_today = False

    #Берем текущую дату и время в необходимом для сравнения варианте
    date = get_current_date()

    result = ''
    for subject in list_of_subjects:
        #Если дата текущая и время меньше, чем начало пары
        if (subject['date'] == date):
            classes_today = True
            result += subject['time'] + ' - ' + subject['name'] + '\n'
        elif classes_today:
            return result
        else:
            return 'There are no lessons today.'

def help_tomorrow():
    #Есть ли сегодня занятия, по умолчанию - нет
    classes_tomorrow = False

    #Берем текущую дату и время в необходимом для сравнения варианте
    date = get_current_date()
    date_arr = date.split('.')
    today = int(date_arr[0])
    today += 1
    date = str(today) + '.' + date_arr[1] + '.' + date_arr[2]

    result = ''
    for subject in list_of_subjects:
        #Если дата текущая и время меньше, чем начало пары
        if (subject['date'] == date):
            classes_tomorrow = True
            result += subject['time'] + ' - ' + subject['name'] + '\n'
    if result != '':
        return result
    else:
        return 'There are no lessons tomorrow.'

def help_week():
    date = list_of_subjects[0]['date']
    flag = False
    result = ''
    for subject in list_of_subjects:
        #Если дата текущая и время меньше, чем начало пары
        if (subject['date'] == date):
            if flag == False:
                result += '\n'+ date + '\n'
                flag = True
            result += subject['time'] + ' - ' + subject['name'] + '\n'
        else:
            flag = False
            
            date_arr = date.split('.')
            today = int(date_arr[0])
            today += 1
            date = str(today) + '.' + date_arr[1] + '.' + date_arr[2]

            if (subject['date'] == date):
                if flag == False:
                    result += date + '\n\n'
                    flag = True
                result += subject['time'] + ' - ' + subject['name'] + '\n'
                
    if result != '':
        return result
    else:
        return 'There are no lessons.'
            

''' ---------ОСНОВНЫЕ ФУНКЦИИ----------- '''
