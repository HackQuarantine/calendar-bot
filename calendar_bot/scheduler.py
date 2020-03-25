import discord
import asyncio
from . import config
from . import calendar
from . import event
import calendar_bot.setup

async def check_schedule():
    await bot.wait_until_ready()
    # Repeat every 60 seconds
    while True:

        cal_event = calendar.check_calendar()
        if cal_event.announcement:
            await send_announcement(event)

        await asyncio.sleep(60)

async def send_announcement(cal_event):

    announcement_channel = bot.get_channel(config.creds['announcement_id'])
    embed = discord.Embed(title=cal_event.title,
                          description=cal_event.description,
                          colour=0x0E1328)
    print("Making announcement for: {}, {}".format(cal_event.title, cal_event.description))
    await announcement_channel.send(embed=embed)
