from datetime import datetime
import sources.py.files as files
import sources.py.groups as groups
from sources.py.tree import *

def gitPush():
    os.system("./../../git-push.sh")

def writeLog(text):
    filename = 'log-' + str(datetime.now().date()) + '.log'
    time = str(datetime.now().time())

    logsFilePath = os.path.join("../..", "logs", filename)

    if os.path.exists(logsFilePath) == True:
        logs = files.loadFile(logsFilePath)
    else:
        groups.update()
        
        logs = {}

    logs[time] = text

    files.saveFile(logs, logsFilePath)