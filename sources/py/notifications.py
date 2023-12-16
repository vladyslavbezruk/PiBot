import asyncio
from datetime import datetime as datef
import sources.py.chats as chats
import sources.py.groups as groups
import sources.py.logs as logs
import sources.py.schedule_func as schedule_func
from main import bot
from sources.py.config import *

async def check(sleep):
    while True:
        await asyncio.sleep(sleep)


        datetime_str = datef.today()
        datetime_obj = datetime_str.strftime("%H%M")

        if datetime_obj == "0000":
            for chat_id in chats.chats.keys():
                try:
                    await bot.send_message(chat_id=chat_id, text='Слава Україні!' + u'\U0001F634')
                except:
                    print("Something went wrong when bot trying send message to user")
            result = groups.update()
            logs.writeLog(result)
            schedule_func.load()
        try:
            await bot.send_message(chat_id='-4000366525', text=f".")
        except:
            print('Error when bot trying to send message .')

        if datef.today().strftime("%A") not in ['Thursday', 'Friday', 'Saturday', 'Sunday']:

            date = schedule_func.get_current_date()
            time = schedule_func.get_current_time()

            for code in schedule_func.schedules.keys():
                schedule = schedule_func.get_subj_list(code)
                name = groups.getName(code)

                max = 0

                for subject in schedule:
                    if subject['date'] == date and schedule_func.get_int_time(
                            subject['time_begin']) - time == time_before:
                        answer = f"⁉Заняття для групи {name} відбудеться через {time_before} хв:\n📢{subject['name']}\n🗓{subject['date']}\n👤{subject['teacher']}\n🕐{subject['time_begin']}-{subject['time_end']}\n⏩{subject['url']}"
                        for chat_id in chats.chats.keys():
                            if name in chats.chats[chat_id]:
                                try:
                                    await bot.send_message(chat_id=chat_id, text=answer)
                                except:
                                    print("Something went wrong when bot trying send message to user")

                    if subject['date'] == date and schedule_func.get_int_time(subject['time_end']) > max:
                        max = schedule_func.get_int_time(subject['time_end'])

                if max == time and max > 0:
                    for chat_id in chats.chats.keys():
                        if name in chats.chats[chat_id]:
                            try:
                                await bot.send_message(chat_id=chat_id, text=f"⁉Заняття для групи {name} закінчились!")
                            except:
                                print("Something went wrong when bot trying send message to user")
                elif max == time and max == 0: 
                    for chat_id in chats.chats.keys():
                        if name in chats.chats[chat_id]:
                            try:
                                await bot.send_message(chat_id=chat_id, text=f"⁉Сьогодні немає занять для групи {name}!")
                            except:
                                print("Something went wrong when bot trying send message to user")
