import json

import asyncio

import codecs

import requests
import urllib3

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    pass

def loadJson(path):
    with codecs.open(path, encoding = 'utf-8') as file:
        data = json.loads(file.read())

    return data

def saveJson(data, path):
    with codecs.open(path, "w", encoding = 'utf-8') as file:
        json.dump(data, file)

def downloadJson(url):
    data = requests.get(url, verify=False)

    return data.json()
