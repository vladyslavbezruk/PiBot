import asyncio
import wolframalpha
from aiogram import Bot, Dispatcher, executor
import sources.py.commands as commands
import sources.py.groups as groups
import sources.py.notifications as notifications
import sources.py.schedule_func as schedule_func
from sources.py.config import *

groups.update()

commands.load()

schedule_func.load()

client = wolframalpha.Client(BOT_WOLF_TOKEN)
loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    print('Bot started!')

    dp.loop.create_task(notifications.check(time_sleep))
    from sources.py.handlers import dp, send_to_admin

    executor.start_polling(dp, on_startup=send_to_admin)