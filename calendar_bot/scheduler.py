import discord
import asyncio
import datetime
import pytz
from . import config
from . import calendar
from . import event
from . import stream
import calendar_bot.setup
from calendar_bot.logging import logger

async def check_schedule():
    await bot.wait_until_ready()
    # Repeat every 60 seconds
    utc = pytz.UTC
    while True:
        now = datetime.datetime.now()
    
        cal_event = calendar.get_next_event(now)
        start_time = cal_event.start.replace(tzinfo=utc)
        if now.replace(tzinfo=utc) == (start_time - datetime.timedelta(minutes=10)).replace(tzinfo=utc):
            await send_announcement(cal_event)
            logger.debug("Send announcement")
        await asyncio.sleep(1)

async def send_announcement(cal_event):

    announcement_channel = bot.get_channel(config.creds['announcement_id'])
    embed = discord.Embed(title=cal_event.title,
                          description=cal_event.description,
                          colour=0x0E1328)
    logger.info(f"Making announcement for: {cal_event.title}, {cal_event.description}")
    await announcement_channel.send(cal_event.get_announcement())
    await announcement_channel.send(embed=embed)
