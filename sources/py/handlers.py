
from random import randrange

from schedule import help_get_url, help_today, help_tomorrow 

import subprocess

from main import bot, dp, client

from aiogram.types import Message, User
from config import admin_id, admin_id2, highmath, discmath, academ, progr, progr02, engl01, engl02, engldate, mathpract, schedule2, schedule1, schedule2json, schedule1json, sUpdate, cpjsons, rmjsons

#from aiogram.methods import SendPhoto
#from aiogram.api.methods import SendPhoto
#from aiogram.api.methods.send_photo import SendPhoto

import time

import wolframalpha

from collections import Counter

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Bot started") 

@dp.message_handler(commands=['start'])
async def echo(message: Message):
    num = randrange(6) + 1
    ur = message.from_user.username

    if f"__{ur}__" != "__None__":
        text = f"@{ur} Hello, {message.from_user.first_name}. Your message - {message.text} (test bot by @vladislavbezruk & @Hokage_Naruto_2020)"
    else:
        text = f"Hello, {message.from_user.first_name}. Your message - {message.text} (test bot by @vladislavbezruk & @Hokage_Naruto_2020)"
    await message.answer(text=text)
    randnum = f"Your random [1-6] number is {num}"
    await message.answer(text=randnum)
    
    await bot.send_message(chat_id=admin_id, text=f"command = start, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['help'])
async def echohelp(message: Message):

    ur = message.from_user.username
 
    await message.answer(text=f"/now - посилання на наступну пару\n/today - пари сьогодні\n/tomorrow - пари завтра\n/schedule1 - розклад ІН-01/1\n/schedule2 - розклад ІН-01/2\n/calc - wolframalpha(Приклад: /calc x^2 = 4)")
    
    await bot.send_message(chat_id=admin_id, text=f"command = help, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['schedule1'])
async def echohelp(message: Message):
    ur = message.from_user.username
    await bot.send_photo(chat_id=message.chat.id, photo=open(schedule1, 'rb'))
    await bot.send_message(chat_id=admin_id, text=f"command = schedule1, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['schedule2'])
async def echohelp(message: Message):
    ur = message.from_user.username
    await bot.send_photo(chat_id=message.chat.id, photo=open(schedule2, 'rb'))
    await bot.send_message(chat_id=admin_id, text=f"command = schedule2, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['calc'])
async def echohelp(message: Message):
    ur = message.from_user.username
    if message.text == "/calc the biggest penis in the universe":
        await bot.send_message(chat_id=message.chat.id, text="Sorry, but the number does not fit in int, but his name is Vladislav Bezruk")
    else:
        query = message.text.replace("/calc ", "")
        res = client.query(query)
        output = next(res.results).text
        await message.answer(text=output)
        await bot.send_message(chat_id=admin_id, text=f"command = calc, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

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

@dp.message_handler(commands=['getid'])
async def echohelp(message: Message):
    await message.answer(text=f"Your id - {str(message.from_user.id)}")

@dp.message_handler(commands=['now'])
async def echohelp(message: Message):
    subprocess.call([f'./{cpjsons}']) 

    result = help_get_url()

    #subject, teacher, url, data, time

    if result != None:
        await message.answer(text=f"{result['subject']}\n{result['date']}\n{result['teacher']}\n{result['time']}\n{result['url']}")
    else: 
        await message.answer(text="There are no lessons today")
  
    subprocess.call([f'./{rmjsons}'])

@dp.message_handler(commands=['today'])
async def echohelp(message: Message):
    subprocess.call([f'./{cpjsons}'])

    result = help_today()

    await message.answer(text=result)

    subprocess.call([f'./{rmjsons}'])

@dp.message_handler(commands=['tomorrow'])
async def echohelp(message: Message):
    subprocess.call([f'./{cpjsons}'])

    result = help_tomorrow()

    await message.answer(text=result)

    subprocess.call([f'./{rmjsons}'])


#@dp.message_handler(commands=['schedule21'])
#async def echohelp(message: Message):
#    ur = message.from_user.username
#    await bot.send_photo(chat_id=message.chat.id, photo=open('schedule21.jpg', 'rb'))
#    await bot.send_message(chat_id=admin_id, text=f"command = schedule21, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

#@dp.message_handler(commands=['schedule22'])
#async def echohelp(message: Message):
#    ur = message.from_user.username
#    await bot.send_photo(chat_id=message.chat.id, photo=open('schedule22.jpg', 'rb'))
#    await bot.send_message(chat_id=admin_id, text=f"command = schedule22, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")
