import datetime
import subprocess
import sys
import time
import os
from math import ceil
from aiogram.types import *
import sources.py.accesses as accesses
import sources.py.chats as chats
import sources.py.commands as commands
import sources.py.keyboard as keyboard
import sources.py.logs as logs
import sources.py.messages as messages
import sources.py.schedule_func as schedule_func
import sources.py.users as users
from main import bot, dp, client
from sources.py.config import *
from sources.py.schedule import *

async def registerMessage(message: Message):
    await message.answer(text=f"🆕{message.from_user.first_name}, Ви новий користувач, ✍️ напишіть команду /start")


async def noAccessMessage(message: Message):
    await message.answer(text=f"⛔️{message.from_user.first_name}, Ви не маєте доступу до цієї команди")


async def invalidGroupMessage(message: Message):
    await message.answer(
        text=f"⁉️{message.from_user.first_name}, у Вас не встановлена група, ✍️ напишіть команду /setgroup (ваша група)")

async def send_to_admin(dp):
    logs.writeLog('Bot started')

    await bot.send_message(chat_id=admin_id, text="Bot started!")


async def mDebug(message: Message):
    log_text = f"message = {message.text} username = @{message.from_user.username} name = {message.from_user.first_name} chat_id = {message.chat.id} user_id = {message.from_user.id}"

    logs.writeLog(log_text)

    await bot.send_message(chat_id=admin_id,
                           text=f"Debug[{message.date}]:\n \tmessage = {message.text}\n \tusername = @{message.from_user.username}\n \tname = {message.from_user.first_name}")

@dp.message_handler(commands=['start'])
async def echo(message: Message):
    await mDebug(message)

    # await bot.send_message(chat_id=message.chat.id, text="Кнопки:", reply_markup=keyboard.keyboard)

    if users.checkUser(message.from_user.id) == False:
        users.addUser('user', message.from_user.id, 'None')

    await message.answer(
        text=f"👋Привіт, {message.from_user.first_name}.\n✍️Відправ мені [/help] для того, щоб отримати список команд")

@dp.message_handler(commands=['help'])
async def echohelp(message: Message):
    await mDebug(message)

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/help') == False:
        await noAccessMessage(message)
        return 0

    if len(message.text) > len("/help "):
        page = int(message.text.replace("/help ", ""))
    else:
        page = 0

    access = users.getAccess(message.from_user.id)

    descriptions = commands.getDescriptions(access)

    count = commands.countCommands(access)

    max_page = ceil(float(count) / commands_page)

    if page + 1 > max_page:
        await message.answer(text='Ви не можете це зробити!')
        return

    i = page * commands_page

    answer = '📜Опис достуних Вам команд:\n'

    while i < (page + 1) * commands_page and i < count:
        answer += descriptions[i]
        i = i + 1

    if (page > 0):
        if page - 1 != 0:
            answer += f'Попередня сторінка: /help {page - 1}\n'
        else:
            answer += 'Попередня сторінка: /help\n'
    if not page + 2 > max_page:
        answer += f'Наступна сторінка: /help {page + 1}\n'

    await message.answer(text=answer)

@dp.message_handler(commands=['about'])
async def echohelp(message: Message):
    await mDebug(message)

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/about') == False:
        await noAccessMessage(message)
        return 0

    await message.answer(
        text='Цей бот був створений студентами спеціальності інформатика Сумського державного університету. ' +
             'Бот допомагає студентам СумДУ отримувати розклад занять у телеграм-чаті. ' +
             'Бот може надсилати автоматичні посилання на заняття до їх початку. ' +
             'Він також вміє розв’язувати математичні приклади і знає відповіді на деякі запитання. ' +
             'Надалі функціонал буде розширюватися.\n' +
             'Автори: @vladyslavbezruk і @starlord0208\n'
             'GitHub: https://github.com/vladyslavbezruk і https://github.com/Ilya-Piskurov'
    )

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

    for schedule in scheduleFilePath:
        logs.writeLog('Sended jsons')

        await bot.send_document(chat_id=message.chat.id, document=open(scheduleFilePath[schedule], 'rb'))

        time.sleep(1)

@dp.message_handler(commands=['restart'])
async def echohelp(message: Message):
    await mDebug(message)

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/restart') == False:
        await noAccessMessage(message)
        return 0

    await message.answer(text=f"Restarting ...")

    accesses.save(accesses.accessesFilePath)
    users.save(users.usersFilePath)

    logs.writeLog('Restaring ...')

@dp.message_handler(commands=['update'])
async def echohelp(message: Message):
    await mDebug(message)

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/update') == False:
        await noAccessMessage(message)
        return 0

    result = groups.update()

    logs.writeLog(result)

    schedule_func.load()

    await message.answer(text=result)

@dp.message_handler(commands=['getSource'])
async def echohelp(message: Message):
    await mDebug(message)

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/getSource') == False:
        await noAccessMessage(message)
        return 0

    logs.writeLog('Sended sources')

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
    await mDebug(message)

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
    await mDebug(message)

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
    await mDebug(message)

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
    await mDebug(message)

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
    await mDebug(message)

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
    await mDebug(message)

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/setgroup') == False:
        await noAccessMessage(message)
        return 0

    group = message.text.replace("/setgroup ", "")

    if (not groups.checkGroup(group)):
        await message.answer(text=f"⁉️{message.from_user.first_name}, немає такої групи")
        return 0

    users.set(users.getAccess(message.from_user.id), message.from_user.id, 'group', str(group))

    await message.answer(text=f"‼️Зараз Ваша група - {group}")

@dp.message_handler(commands=['setLink'])
async def echohelp(message: Message):
    await mDebug(message)

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/setLink') == False:
        await noAccessMessage(message)
        return 0

    args = message.text.replace("/setLink ", "").split(", ")
    group = args[0]
    subject = args[1]
    link = args[2]

    if (not groups.checkGroup(group)):
        await message.answer(text=f"⁉️{message.from_user.first_name}, немає такої групи")
        return 0

    groups.setLink(group, subject, link)

    await message.answer(text=f"‼️Посилання встановлено")

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

@dp.message_handler(commands=['addGroup'])
async def echohelp(message: Message):
    await mDebug(message)

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/addGroup') == False:
        await noAccessMessage(message)
        return 0

    group = str(message.text.replace("/addGroup ", ""))
    chat_id = str(message.chat.id)

    if (not groups.checkGroup(group)):
        await message.answer(text=f"Немає такої групи як {group}")
        return
    if chats.checkGroup(chat_id, group) == False:
        chats.addGroup(chat_id, group)
        await message.answer(text=f"Група {group} додана для автоматичного сповіщення в цьому чаті")
    else:
        await message.answer(text=f"Група {group} вже була додана для автоматичного сповіщення в цьому чаті")

@dp.message_handler(commands=['removeGroup'])
async def echohelp(message: Message):
    await mDebug(message)

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/removeGroup') == False:
        await noAccessMessage(message)
        return 0

    group = str(message.text.replace("/removeGroup ", ""))
    chat_id = str(message.chat.id)

    if chats.checkGroup(chat_id, group) == True:
        chats.removeGroup(chat_id, group)
        await message.answer(text=f"Група {group} видалена для автоматичного сповіщення в цьому чаті")
    else:
        await message.answer(text=f"Група {group} вже була видалена для автоматичного сповіщення в цьому чаті")

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

    group = groups.getCode(str(group))

    result = help_get_url(str(group))

    await message.answer(result)

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

    group = groups.getCode(str(group))

    result = help_today(str(group))
    await message.answer(text=result)

@dp.message_handler(commands=['date'])
async def echohelp(message: Message):
    await mDebug(message)

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

    group = groups.getCode(str(group))

    result = help_date(str(group), message.text.replace("/date ", ""))
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

    group = groups.getCode(str(group))

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

    group = groups.getCode(str(group))

    result = help_week(str(group))
    await message.answer(text=result)

@dp.message_handler(commands=['send'])
async def echohelp(message: Message):
    await mDebug(message)

    if users.checkUser(message.from_user.id) == False:
        await registerMessage(message)
        return 0

    if users.checkCommand(message.from_user.id, '/send') == False:
        await noAccessMessage(message)
        return 0

    messages.push(message)

    text_message = message.text.replace("/send ", "")

    text = f"⁉Message:\nusername = @{message.from_user.username} name = {message.from_user.first_name} chat_id = {message.chat.id} user_id = {message.from_user.id}\nMessage: {text_message}"
    await bot.send_message(chat_id=admin_id, text=text)

    await message.answer(text='Анонімне повідомлення відправлено!')

@dp.message_handler(content_types=ContentType.TEXT)
async def echoMessage(message: Message):
    await mDebug(message)

    if chats.checkChat(message.chat.id) == False:
        chats.addChat(message.chat.id)

        await bot.send_message(chat_id=message.chat.id, text="Кнопки:", reply_markup=keyboard.keyboard)
