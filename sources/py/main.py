import asyncio

import wolframalpha

#import json_func

import users

#import groups 

from aiogram import Bot, Dispatcher, executor
from config import *

import schedule_func

schedule_func.load()

#json_func.sorting(1)
#json_func.sorting(2)

#groups.updatingGroupsList(usersFilePath, groupsFilePath)

client = wolframalpha.Client(BOT_WOLF_TOKEN)
loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)


