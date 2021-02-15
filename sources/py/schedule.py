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

help_week()
Возвращает строку в которой перечень занятий на неделю
'''

from schedule_func import *

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
            return 'There are no lessons today'

def help_tomorrow():
    #Есть ли сегодня занятия, по умолчанию - нет
    classes_tomorrow = False

    #Берем текущую дату и время в необходимом для сравнения варианте
    date = get_current_date()
    date = date_tomorrow(date)

    result = ''
    for subject in list_of_subjects:
        #Если дата текущая и время меньше, чем начало пары
        if (subject['date'] == date):
            classes_tomorrow = True
            result += subject['time'] + ' - ' + subject['name'] + '\n'
    if result != '':
        return result
    else:
        return 'There are no lessons tomorrow'

def help_week():
    date = list_of_subjects[0]['date']
    flag = False
    result = 'Розклад:\n'
    
    for subject in list_of_subjects:
        #Если дата текущая и время меньше, чем начало пары
        if (subject['date'] == date):
            if flag == False:
                result += '\n' + date + ':\n'
                flag = True
            result += subject['time'] + ' - ' + subject['name'] + '\n'
        else:
            flag = False
            
            date = date_tomorrow(date)

            if (subject['date'] == date):
                if flag == False:
                    result += '\n' + date + ':\n'
                    flag = True
                result += subject['time'] + ' - ' + subject['name'] + '\n'
                
    if result != '':
        return result
    else:
        return 'There are no lessons'

