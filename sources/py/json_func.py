import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

import config

def load(id):
    with codecs.open(config.scheduleFilePath[str(id)], encoding='utf-8') as schedule_file:
        #Сохраняем расписание в виде словаря Python
        schedule = json.loads(schedule_file.read())
    return schedule
    
def save(schedule, id):
    with codecs.open(config.scheduleFilePath[str(id)], "w", encoding='utf-8') as schedule_wfile:
        json.dump(schedule, schedule_wfile)

