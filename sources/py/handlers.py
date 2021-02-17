'''
Основной модуль для работы с ботом.
Тут функции, которые осущетвляют ввод-вывод в Телеграм.
Остальную логику разбивать по модулям.
'''

from random import randrange

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

#Сообщение о включении бота
async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Bot started!") 

async def mDebug(message: Message):
    await bot.send_message(chat_id=admin_id, text=f"Debug[{message.date}]:\n \tmessage = {message.text}\n \tusername = @{message.from_user.username}\n \tname = {message.from_user.first_name}")

@dp.message_handler(commands=['start'])
async def echo(message: Message):
    '''
    num = randrange(6) + 1

    if f"__{message.from_user.username}__" != "__None__":
        text = f"@{message.from_user.username} Hello, {message.from_user.first_name}. Your message - {message.text} (test bot by @vladislavbezruk & @Hokage_Naruto_2020)"
    else:
        text = f"Hello, {message.from_user.first_name}. Your message - {message.text} (test bot by @vladislavbezruk & @Hokage_Naruto_2020)"
    await message.answer(text=text)
    randnum = f"Your random [1-6] number is {num}"
    await message.answer(text=randnum)
    '''
    await message.answer(text=f"Hello, {message.from_user.first_name}.\nSend me [/help] to find out all the commands")
    await mDebug(message)
   #await bot.send_message(chat_id=admin_id, text=f"command = start, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['help'])
async def echohelp(message: Message):
 
    await message.answer(text=f"/now [group] - посилання на наступну пару(Приклад: /now 1)\n/today [group] - пари сьогодні(Приклад: /today 1)\n/tomorrow [group] - пари завтра(Приклад: /tomorrow 1)\n/schedule1 - розклад ІН-01/1\n/schedule2 - розклад ІН-01/2\n/week [group] - розклад на тиждень(Приклад: /week 1)\n/calc [question] - wolframalpha(Приклад: /calc x^2 = 4)")
    
    #await bot.send_message(chat_id=admin_id, text=f"command = help, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")
    await mDebug(message)

@dp.message_handler(commands=['schedule1'])
async def echohelp(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open(schedule1, 'rb'))
    #await bot.send_message(chat_id=admin_id, text=f"command = schedule1, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")
    await mDebug(message)

@dp.message_handler(commands=['schedule2'])
async def echohelp(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open(schedule2, 'rb'))
   #await bot.send_message(chat_id=admin_id, text=f"command = schedule2, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")
    await mDebug(message)

@dp.message_handler(commands=['calc'])
async def echohelp(message: Message):
    
    query = message.text.replace("/calc ", "")
    res = client.query(query)
    output = next(res.results).text
    await message.answer(text=output)
    #await bot.send_message(chat_id=admin_id, text=f"command = calc, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")
    await mDebug(message)

@dp.message_handler(commands=['getjson'])
async def echohelp(message: Message):
    if message.from_user.id == admin_id:
        await bot.send_document(chat_id=message.chat.id, document=open(schedule1json, 'rb'))
        await bot.send_document(chat_id=message.chat.id, document=open(schedule2json, 'rb'))
    elif message.from_user.id == admin_id2:
        await bot.send_document(chat_id=message.chat.id, document=open(schedule1json, 'rb'))
        await bot.send_document(chat_id=message.chat.id, document=open(schedule2json, 'rb'))
    else:
        await message.answer(text="Sorry, you're not the admin")
    await mDebug(message)

@dp.message_handler(commands=['update'])
async def echohelp(message: Message):
    if message.from_user.id == admin_id:
        subprocess.call([f'./{sUpdate}'])
        await message.answer(text="Schedules updated")
    elif message.from_user.id == admin_id2:
        subprocess.call([f'./{sUpdate}'])
        await message.answer(text="Schedules updated")
    else:
        await message.answer(text="Sorry, you're not the admin")
    await mDebug(message)

@dp.message_handler(commands=['getSource'])
async def echohelp(message: Message):
    if message.from_user.id == admin_id:
        subprocess.call(['./createSource.sh'])
        await bot.send_document(chat_id=message.chat.id, document=open('PiBot.zip', 'rb'))
    elif message.from_user.id == admin_id2:
        subprocess.call(['./createSource.sh'])
        await bot.send_document(chat_id=message.chat.id, document=open('PiBot.zip', 'rb'))
    else:
        await message.answer(text="Sorry, you're not the admin")
    await mDebug(message)

def compare(a, b, size):
    for i in range(size):
        if a[i] != b[i]:
            return False

    return True

@dp.message_handler(commands=['shutdown'])
async def echohelp(message: Message):

    time = datetime.now()

    if compare(str(time), str(message.date), 18):
        if message.from_user.id == admin_id:
            await message.answer(text="Goodbye ...")
            subprocess.call(['reboot'])
        elif message.from_user.id == admin_id2:
            await message.answer(text="Goodbye ...")
            subprocess.call(['reboot'])
        else:
            await message.answer(text="Sorry, you're not the admin")
    await mDebug(message)

@dp.message_handler(commands=['getid'])
async def echohelp(message: Message):
    await message.answer(text=f"Your id - {str(message.from_user.id)}")
    await mDebug(message)

@dp.message_handler(commands=['now'])
async def echohelp(message: Message):
    result = help_get_url(message.text.replace("/now ", ""))
    
    if result != None:
        await message.answer(text=f"{result['subject']}\n{result['date']}\n{result['teacher']}\n{result['time']}\n{result['url']}")
    else: 
        await message.answer(text="There are no lessons today")
    await mDebug(message)

@dp.message_handler(commands=['today'])
async def echohelp(message: Message):
    result = help_today(message.text.replace("/today ", ""))
    await message.answer(text=result)
    await mDebug(message)

@dp.message_handler(commands=['tomorrow'])
async def echohelp(message: Message):
    result = help_tomorrow(message.text.replace("/tomorrow ", ""))
    await message.answer(text=result)
    await mDebug(message)

@dp.message_handler(commands=['week'])
async def echohelp(message: Message):
    result = help_week(message.text.replace("/week ", ""))
    await message.answer(text=result)
    await mDebug(message)
