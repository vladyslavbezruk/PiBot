import json

import requests

import asyncio

import codecs

def loadJson(path):
    with codecs.open(path, encoding = 'utf-8') as file:
        data = json.loads(file.read())

    return data

def saveJson(data, path):
    with codecs.open(path, "w", encoding = 'utf-8') as file:
        json.dump(data, file)

def downloadJson(url):
    data = requests.get(url)

    return data.json()