
from random import randrange

import subprocess

from main import bot, dp, client

from aiogram.types import Message, User
from config import admin_id, admin_id2, highmath, discmath, academ, progr, progr02, engl01, engl02, engldate, mathpract, schedule2, schedule1, schedule2json, schedule1json, sUpdate

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
 
    await message.answer(text=f"/help1 - Вища мат. (лек.)\n/help2 - Вища мат. (практ.)\n/help3 - Дискр. мат. (all)\n/help4 - Акад. письмо (практ.)\n/help5 - Програм. (лек. + практ. /1)\n/help6 - Програм. (практ. /2)\n/help7 - Англ. (практ. /2, only for {engldate})\n/help8 - Англ. (практ. /1)\n/schedule1 - розклад ІН-01/1\n/schedule2 - розклад ІН-01/2")
    
    await bot.send_message(chat_id=admin_id, text=f"command = help, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['help1'])
async def echohelp(message: Message):
    ur = message.from_user.username
    await message.answer(text=highmath)
    await bot.send_message(chat_id=admin_id, text=f"command = help1, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['help2'])
async def echohelp(message: Message):
    ur = message.from_user.username
    await message.answer(text=mathpract)
    await bot.send_message(chat_id=admin_id, text=f"command = help2, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['help3'])
async def echohelp(message: Message):
    ur = message.from_user.username
    await message.answer(text=discmath)
    await bot.send_message(chat_id=admin_id, text=f"command = help3, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['help4'])
async def echohelp(message: Message):
    ur = message.from_user.username
    await message.answer(text=academ)
    await bot.send_message(chat_id=admin_id, text=f"command = help4, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['help5'])
async def echohelp(message: Message):
    ur = message.from_user.username
    await message.answer(text=progr)
    await bot.send_message(chat_id=admin_id, text=f"command = help5, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['help6'])
async def echohelp(message: Message):
    ur = message.from_user.username
    await message.answer(text=progr02)
    await bot.send_message(chat_id=admin_id, text=f"command = help6, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['help7'])
async def echohelp(message: Message):
    ur = message.from_user.username
    await message.answer(text=engl02)
    await bot.send_message(chat_id=admin_id, text=f"command = help7, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

@dp.message_handler(commands=['help8'])
async def echohelp(message: Message):
    ur = message.from_user.username
    await message.answer(text=engl01)
    await bot.send_message(chat_id=admin_id, text=f"command = help8, username = {ur}, name = {message.from_user.first_name}, date = {str(message.date)}")

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
