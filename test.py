from telethon import TelegramClient
from telethon.tl.types import UserStatusOnline, UserStatusOffline, ContactStatus
from datetime import datetime
from time import sleep
import asyncio

async def check():
    api_id = 18878839
    api_hash = '91b564be28488684ee36e71ff43891fe'

    while(1):
        sleep(5)
        async with TelegramClient('anon', api_id, api_hash) as client:
        #client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))

            user = await client.get_entity('podoliak_anhelina')

            try:
                if isinstance(user.status, UserStatusOnline):
                    print("Online")
                elif isinstance(user.status, UserStatusOffline):
                    print(str(user.status.was_online).replace("+00:00", ""))
                else:
                    print('Unable to get last seen')
            except:
                    print("Unable to get last seen")


loop = asyncio.get_event_loop()
loop.run_until_complete(check())
loop.close()
