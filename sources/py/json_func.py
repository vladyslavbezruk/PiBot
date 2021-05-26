import json

import asyncio

import codecs

import requests
import urllib3

import files

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    pass

def loadJson(path):
    data = files.loadFile(path)

    return data

def saveJson(data, path):
    files.saveFile(data, path)

def downloadJson(url):
    data = requests.get(url, verify=False)

    return data.json()
