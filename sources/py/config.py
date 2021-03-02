'''
Модуль, где храним конфигурации (константы)
'''

import os

BOT_TOKEN = "1587405934:AAEAKvidxADTdlu_Pr0w8TQHpO-QV7T4uEM" 
BOT_WOLF_TOKEN = "P8PX47-KP489EE3R6"

sUpdate = "../sh/update.sh"

admin_id  = 671836800
admin_id2 = 761202580

schedule2 = "../../resources/media/schedule2.jpg"
schedule1 = "../../resources/media/schedule1.jpg"

schedule2json = "../../resources/json/schedule2.json"
schedule1json = "../../resources/json/schedule1.json"

subjects = "../../resources/json/subjects.json"

createSource = "../sh/createSource.sh"

removeSource = "../sh/removeSource.sh"

scheduleFilePath = {}
scheduleFilePath['1'] = os.path.join("..", "..", "resources", "json", "schedule1.json")
scheduleFilePath['2'] = os.path.join("..", "..", "resources", "json", "schedule2.json")

usersFilePath = os.path.join("..", "..", "resources", "json", "users.json")

groupsFilePath = os.path.join("..", "..", "resources", "json", "groups.json")

subjectsFilePath = os.path.join("..", "..", "resources", "json", "subjects.json")
