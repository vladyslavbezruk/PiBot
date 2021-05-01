'''
Основной модуль для работы с ботом.
Тут функции, которые осущетвляют ввод-вывод в Телеграм.
Остальную логику разбивать по модулям.
'''

from random import randrange

import users
import accesses

import keyboard

import sys

import notifications

import datetime

from schedule import * 

import schedule_func

import subprocess

from main import bot, dp, client

from aiogram.types import *

from config import *

import time

import wolframalpha

import chats

import logs

#import json_func

from collections import Counter

async def registerMessage(message: Message):
    await message.answer(text=f"🆕{message.from_user.first_name}, Ви новий користувач, ✍️ напишіть команду /start")

async def noAccessMessage(message: Message):
    await message.answer(text=f"⛔️{message.from_user.first_name}, Ви не маєте доступу до цієї команди")

async def invalidGroupMessage(message: Message):
    await message.answer(text=f"⁉️{message.from_user.first_name}, у Вас не встановлена група, ✍️ напишіть команду /setgroup (ваша група)")

#Сообщение о включении бота
async def send_to_admin(dp):
    logs.writeLog('Bot started')

    await bot.send_message(chat_id=admin_id, text="Bot started!")

async def mDebug(message: Message):
    log_text = f"message = {message.text} username = @{message.from_user.username} name = {message.from_user.first_name} chat_id = {message.chat.id} user_id = {message.from_user.id}"

    logs.writeLog(log_text)

    await bot.send_message(chat_id=admin_id, text=f"Debug[{message.date}]:\n \tmessage = {message.text}\n \tusername = @{message.from_user.username}\n \tname = {message.from_user.first_name}")

@dp.message_handler(commands=['start'])
async def echo(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Кнопки:", reply_markup=keyboard.keyboard)

    if users.checkUser(message.from_user.id) == False:
        users.addUser('user', message.from_user.id, 'None')

    await message.answer(text=f"👋Hello, {message.from_user.first_name}.\n✍️Send me [/help] to find out all the commands")

@dp.message_handler(commands=['help'])
async def echohelp(message: Message):
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/help') == False:
        await noAccessMessage(message)
        return 0
 
    await message.answer(text=f"📜Перелік найважливіших команд:\n" +
        "✳️/now - посилання на наступну пару\n" +
        "✳️/today - пари сьогодні\n" +
        "✳️/tomorrow - пари завтра\n" +
        "✳️/date - розклад по даті (Приклад: /date 08.03.2021)\n" +
        "✳️/week - розклад на тиждень\n" +
        "✳️/setgroup [group] - встановити групу (Приклад: /setgroup 1)\n" +
        " ✅ /setgroup 1 - для групи ІН-01/1\n" +
        " ✅ /setgroup 2 - для групи ІН-01/2\n" +
        "✳️/calc [question] - wolframalpha (Приклад: /calc x^2 = 4)")

@dp.message_handler(commands=['calc'])
async def echohelp(message: Message):
    
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
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/getjson') == False:
        await noAccessMessage(message)
        return 0

    for schedule in scheduleFilePath:
        logs.writeLog('Sended jsons')

        await bot.send_document(chat_id=message.chat.id, document=open(scheduleFilePath[schedule], 'rb'))

@dp.message_handler(commands=['update'])
async def echohelp(message: Message):
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/update') == False:
        await noAccessMessage(message)
        return 0
   
    subprocess.call([f'./{sUpdate}'])

    logs.writeLog('Schedules updated')

    schedule_func.load()

    await message.answer(text="Schedules updated")
   
@dp.message_handler(commands=['getSource'])
async def echohelp(message: Message):
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/getSource') == False:
        await noAccessMessage(message)
        return 0

    logs.writeLog('Sended source')

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

        logs.writeLog('Shutdown ...')

        sys.exit(0)
        return

@dp.message_handler(commands=['getAccess'])
async def echohelp(message: Message):

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/getAccess') == False:
        await noAccessMessage(message)
        return 0

    access = users.getAccess(message.from_user.id)
    await message.answer(text=f"Your access level - {access}")

@dp.message_handler(commands=['getCommands'])
async def echohelp(message: Message):

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/getCommands') == False:
        await noAccessMessage(message)
        return 0

    commands = accesses.getCommands(users.getAccess(message.from_user.id))

    await message.answer(text=commands)

@dp.message_handler(commands=['getCommandsAccess'])
async def echohelp(message: Message):

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/getCommandsAccess') == False:
        await noAccessMessage(message)
        return 0

    commands = accesses.getCommands(message.text.replace("/getCommandsAccess ", ""))

    await message.answer(text=commands)

@dp.message_handler(commands=['save'])
async def echohelp(message: Message):
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/save') == False:
        await noAccessMessage(message)
        return 0

    logs.writeLog('Saving data ...')

    accesses.save(accesses.accessesFilePath)
    users.save(users.usersFilePath)
    
    await message.answer(text="All saved!")

@dp.message_handler(commands=['setgroup'])
async def echohelp(message: Message):
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/setgroup') == False:
        await noAccessMessage(message)
        return 0
        
    group = message.text.replace("/setgroup ", "")

    if (group != '1' and group != '2'):
        await message.answer(text=f"⁉️{message.from_user.first_name}, номер групи має бути 1 або 2")
        return 0

    users.set(users.getAccess(message.from_user.id), message.from_user.id, 'group', str(group))

    await message.answer(text=f"‼️Зараз Ваша група - ІН-01/{group}")

@dp.message_handler(commands=['getid'])
async def echohelp(message: Message):
    
    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0
        
    if users.checkCommand(message.from_user.id, '/getid') == False:
        await noAccessMessage(message)
        return 0
        
    await message.answer(text=f"Your id - {str(message.from_user.id)}")
    
@dp.message_handler(commands=['addGroup'])
async def echohelp(message: Message):

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/addGroup') == False:
        await noAccessMessage(message)
        return 0

    group = message.text.replace("/addGroup ", "")

    if chats.checkGroup(message.chat.id, group) == False:
        chats.addGroup(message.chat.id, group)
        await message.answer(text=f"Група {group} додана для автоматичного сповіщення в цьому чаті")
    else:
        await message.answer(text=f"Група {group} вже була додана для автоматичного сповіщення в цьому чаті")

@dp.message_handler(commands=['removeGroup'])
async def echohelp(message: Message):

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/removeGroup') == False:
        await noAccessMessage(message)
        return 0

    group = message.text.replace("/removeGroup ", "")

    if chats.checkGroup(message.chat.id, group) == True:
        chats.removeGroup(message.chat.id, group)
        await message.answer(text=f"Група {group} видалена для автоматичного сповіщення в цьому чаті")
    else:
        await message.answer(text=f"Група {group} вже була видалена для автоматичного сповіщення в цьому чаті")

@dp.message_handler(commands=['now'])
async def echohelp(message: Message):
    
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
    
    await message.answer(result)

@dp.message_handler(commands=['today'])
async def echohelp(message: Message):
    
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

@dp.message_handler(commands=['date'])
async def echohelp(message: Message):

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/date') == False:
        await noAccessMessage(message)
        return 0

    group = users.get(users.getAccess(message.from_user.id), message.from_user.id, 'group')

    if group == 'None':
        await invalidGroupMessage(message)
        return 0

    result = help_date(str(group), message.text.replace("/date ", ""))
    await message.answer(text=result)

@dp.message_handler(commands=['tomorrow'])
async def echohelp(message: Message):

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

@dp.message_handler(content_types = ContentType.TEXT)
async def echoMessage(message: Message):
    await mDebug(message)

    if chats.checkChat(message.chat.id) == False:
        chats.addChat(message.chat.id)

        await bot.send_message(chat_id=message.chat.id, text="Кнопки:", reply_markup = keyboard.keyboard)