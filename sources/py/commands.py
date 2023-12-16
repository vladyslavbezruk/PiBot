import sources.py.accesses as accesses
import sources.py.files as files
from sources.py.config import *
from sources.py.tree import *

descriptions = {}

def load():
    global descriptions

    descriptions = files.loadFile(descriptionsFilePath)

def getDescriptions(access):
    answer = {}

    i = 0

    for command in accesses.accesses[access]:
        answer[i] = clause + f' {command}: {descriptions[command]}\n'

        i = i + 1

    return answer

def countCommands(access):
    return len(accesses.accesses[access])