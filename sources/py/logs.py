import json    #Работаем с json

import codecs  #Читаем с учетом кодировки

from datetime import datetime

import os

import accesses

import files

from aiogram.types import *

from config import *

import groups

from tree import *

def gitPush():
    os.system("./../../git-push.sh")

def writeLog(text):
    filename = 'log-' + str(datetime.now().date()) + '.log'
    time = str(datetime.now().time())

    logsFilePath = os.path.join("..", "..", "logs", filename)

    if os.path.exists(logsFilePath) == True:
        logs = files.loadFile(logsFilePath)
    else:
        groups.update()
        gitPush()

        logs = {}

    logs[time] = text

    files.saveFile(logs, logsFilePath)