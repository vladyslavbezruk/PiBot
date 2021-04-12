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
def help_get_url(id):
    schedule = get_subj_list(id)

    #Есть ли сегодня занятия, по умолчанию - нет
    classes_today = False

    #Берем текущую дату и время в необходимом для сравнения варианте
    date = get_current_date()
    time = get_current_time()
    
    for subject in schedule:
        #Если дата текущая и время меньше, чем начало пары
        if subject['date'] == date and time < get_int_time(subject['time_end']):
            classes_today = True
            break
    if classes_today:
        return f"🔜Найближче заняття для групи ІН-01/{id}\n📢{subject['name']}\n🗓{subject['date']}\n👤{subject['teacher']}\n🕐{subject['time_begin']}-{subject['time_end']}\n⏩{subject['url']}"
    else:
        return f'⛔Сьогодні вже немає наступних занять для групи ІН-01/{id}'

def help_today(id):
    schedule = get_subj_list(id)
    
    #Есть ли сегодня занятия, по умолчанию - нет
    classes_today = False

    #Берем текущую дату и время в необходимом для сравнения варианте
    date = get_current_date()

    result = f'⏱Розклад на сьогодні для групи ІН-01/{id}\n' 
    for subject in schedule:
        #Если дата текущая и время меньше, чем начало пары
        if (subject['date'] == date):
            classes_today = True
            result += ' ✅ ' + subject['time_begin'] + '-' + subject['time_end'] + ' - ' + subject['name'] + '\n'

    if classes_today == True:
        return result
    else:
        return f'⛔️Сьогодні немає занять для групи ІН-01/{id}'

def help_tomorrow(id):
    schedule = get_subj_list(id)

    #Есть ли сегодня занятия, по умолчанию - нет
    classes_tomorrow = False

    #Берем текущую дату и время в необходимом для сравнения варианте
    date = get_current_date()
    date = date_tomorrow(date)

    result = f'⏱Розклад на завтра для групи ІН-01/{id}\n'
    for subject in schedule:
        #Если дата текущая и время меньше, чем начало пары
        if (subject['date'] == date):
            classes_tomorrow = True
            result += ' ✅ ' + subject['time_begin'] + '-' + subject['time_end'] + ' - ' + subject['name'] + '\n'
    if result != f'⏱Розклад на завтра для групи ІН-01/{id}\n':
        return result
    else:
        return f'⛔Завтра немає занять для групи ІН-01/{id}'

def help_week(id):
    schedule = get_subj_list(id)

    date = schedule[0]['date']
    flag = False
    result = f'⏱Розклад на тиждень для групи ІН-01/{id}\n'

    for subject in schedule:
        if (subject['date'] == date):
            if flag == False:
                result += '\n' + date + ':\n'
                flag = True
            result += ' ✅ ' + subject['time_begin'] + '-' + subject['time_end'] + ' - ' + subject['name'] + '\n'
        else:
            flag = False
            
            date = subject['date']

            if (subject['date'] == date):
                if flag == False:
                    result += '\n' + date + ':\n'
                    flag = True
                result += ' ✅ ' + subject['time_begin'] + '-' + subject['time_end'] + ' - ' + subject['name'] + '\n'
                
    if result != f'⏱Розклад на тиждень для групи ІН-01/{id}\n':
        return result
    else:
        return f'⛔На цей тиджень немає занять для групи ІН-01/{id}'

def help_date(id, date):
    schedule = get_subj_list(id)
    
    flag = False

    result = f'⏱РРозклад на {date} для групи ІН-01/{id}\n'

    for subject in schedule:
        if (subject['date'] == date):
            flag = True
            result += ' ✅ ' + subject['time_begin'] + '-' + subject['time_end'] + ' - ' + subject['name'] + '\n'

    if flag == True:
        return result
    else:
        return f'⛔На {date} немає занять для групи ІН-01/{id}'
