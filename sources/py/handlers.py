'''
Основной модуль для работы с ботом.
Тут функции, которые осущетвляют ввод-вывод в Телеграм.
Остальную логику разбивать по модулям.
'''

from random import randrange

import users
import accesses

import sys

import datetime

from schedule import * 

import subprocess

from main import bot, dp, client

from aiogram.types import Message, User

from config import *

import time

import wolframalpha

from collections import Counter

async def registerMessage(message: Message):
    await message.answer(text=f"{message.from_user.first_name}, you are a new user, write the command /start")

async def noAccessMessage(message: Message):
    await message.answer(text=f"{message.from_user.first_name}, you do not have access to this command")

async def invalidGroupMessage(message: Message):
    await message.answer(text=f"{message.from_user.first_name}, pls write the command /setgroup (your group)")

#Сообщение о включении бота
async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Bot started!") 

async def mDebug(message: Message):
    await bot.send_message(chat_id=admin_id, text=f"Debug[{message.date}]:\n \tmessage = {message.text}\n \tusername = @{message.from_user.username}\n \tname = {message.from_user.first_name}")

@dp.message_handler(commands=['start'])
async def echo(message: Message):

    if users.checkUser(message.from_user.id) == False:
        users.addUser('user', message.from_user.id, 'None')
    
    await message.answer(text=f"Hello, {message.from_user.first_name}.\nSend me [/help] to find out all the commands")
    await mDebug(message)

@dp.message_handler(commands=['help'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/help') == False:
        await noAccessMessage(message)
        return 0
 
    await message.answer(text=f"/now - посилання на наступну пару(Приклад: /now 1)\n" +
        "/today - пари сьогодні(Приклад: /today 1)\n" +
        "/tomorrow - пари завтра(Приклад: /tomorrow 1)\n" +
        "/schedule1 - розклад ІН-01/1\n/schedule2 - розклад ІН-01/2\n" +
        "/week - розклад на тиждень(Приклад: /week 1)\n" +
        "/setgroup [group] - встановити групу(Приклад: /setgroup 1)\n" +
        "/calc [question] - wolframalpha(Приклад: /calc x^2 = 4)")

@dp.message_handler(commands=['calc'])
async def echohelp(message: Message):
    
    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/calc') == False:
        await noAccessMessage(message)
        return 0
  
    query = message.text.replace("/calc ", "")
    res = client.query(query)
    output = next(res.results).text
    await message.answer(text=output)

@dp.message_handler(commands=['getjson'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/getjson') == False:
        await noAccessMessage(message)
        return 0

    await bot.send_document(chat_id=message.chat.id, document=open(schedule1json, 'rb'))
    await bot.send_document(chat_id=message.chat.id, document=open(schedule2json, 'rb'))

@dp.message_handler(commands=['update'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/update') == False:
        await noAccessMessage(message)
        return 0
   
    subprocess.call([f'./{sUpdate}'])
    await message.answer(text="Schedules updated")
   
@dp.message_handler(commands=['getSource'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/getSource') == False:
        await noAccessMessage(message)
        return 0

    subprocess.call([f'./{createSource}'])
    await bot.send_document(chat_id=message.chat.id, document=open('../../PiBot.zip', 'rb'))
    subprocess.call([f'./{removeSource}'])

def compare(a, b, size):
    for i in range(size):
        if a[i] != b[i]:
            return False

    return True

@dp.message_handler(commands=['shutdown'])
async def echohelp(message: Message):

    time = datetime.now()
    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/shutdown') == False:
        await noAccessMessage(message)
        return 0

    if compare(str(time), str(message.date), 18):
        await message.answer(text="Goodbye ...")
 
        accesses.save(accesses.accessesFilePath)
        users.save(users.usersFilePath)

        sys.exit(0)
        return
        
@dp.message_handler(commands=['save'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/save') == False:
        await noAccessMessage(message)
        return 0

    accesses.save(accesses.accessesFilePath)
    users.save(users.usersFilePath)
    
    await message.answer(text="All saved!")

@dp.message_handler(commands=['setgroup'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/setgroup') == False:
        await noAccessMessage(message)
        return 0
        
    group = message.text.replace("/setgroup ", "")
    users.set(users.getAccess(message.from_user.id), message.from_user.id, 'group', str(group))

    await message.answer(text=f"Now your group - {group}")

@dp.message_handler(commands=['getid'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/getid') == False:
        await noAccessMessage(message)
        return 0
        
    await message.answer(text=f"Your id - {str(message.from_user.id)}")
    
@dp.message_handler(commands=['now'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/now') == False:
        await noAccessMessage(message)
        return 0
    
    group = users.get(users.getAccess(message.from_user.id), message.from_user.id, 'group')

    if group == 'None':
        await invalidGroupMessage(message)
        return 0

    result = help_get_url(str(group))
    
    if result != None:
        await message.answer(text=f"{result['subject']}\n{result['date']}\n{result['teacher']}\n{result['time']}\n{result['url']}")
    else: 
        await message.answer(text="There are no lessons today")

@dp.message_handler(commands=['today'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/today') == False:
        await noAccessMessage(message)
        return 0
    
    group = users.get(users.getAccess(message.from_user.id), message.from_user.id, 'group')

    if group == 'None':
        await invalidGroupMessage(message)
        return 0

    result = help_today(str(group))
    await message.answer(text=result)

@dp.message_handler(commands=['tomorrow'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/tomorrow') == False:
        await noAccessMessage(message)
        return 0
    
    group = users.get(users.getAccess(message.from_user.id), message.from_user.id, 'group')

    if group == 'None':
        await invalidGroupMessage(message)
        return 0

    result = help_tomorrow(str(group))
    await message.answer(text=result)

@dp.message_handler(commands=['week'])
async def echohelp(message: Message):

    await mDebug(message)
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/week') == False:
        await noAccessMessage(message)
        return 0

    group = users.get(users.getAccess(message.from_user.id), message.from_user.id, 'group')

    if group == 'None':
        await invalidGroupMessage(message)
        return 0

    result = help_week(str(group))
    await message.answer(text=result)
