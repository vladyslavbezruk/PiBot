import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from datetime import datetime

import os

import accesses

from aiogram.types import *

from config import *

def writeLog(text):
    filename = 'log-' + str(datetime.now().date()) + '.log'
    time = str(datetime.now().time())

    logsFilePath = os.path.join("..", "..", "logs", filename)

    if os.path.exists(logsFilePath) == True:
        with codecs.open(logsFilePath, encoding='utf-8') as logs_file:
            logs = json.loads(logs_file.read())
    else:
        logs = {}

    logs[time] = text

    with codecs.open(logsFilePath, "w", encoding='utf-8') as logs_file:
        json.dump(logs, logs_file)