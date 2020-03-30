import discord
import asyncio
import datetime
import dateutil.parser
import pytz
from . import config
from . import calendar
from . import event
from . import stream
import calendar_bot.setup
from calendar_bot.logging import logger

async def check_schedule():
    await bot.wait_until_ready()
    while True:
        now = datetime.datetime.now()
    
        cal_event = calendar.get_next_event(now)
        current_time = dateutil.parser.parse(now.strftime("%Y-%m-%d %H:%M:%S"))
        start_time = cal_event.start
        announcement_time = (start_time - datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
        
        logger.debug(f'{current_time} : Now')
        logger.debug(f'{announcement_time} : Message time')
        
        if current_time == announcement_time:
            await send_announcement(cal_event)
            logger.debug("Send announcement")
        await asyncio.sleep(0.2)

async def send_announcement(cal_event):

    announcement_channel = bot.get_channel(config.creds['announcement_id'])
    embed = discord.Embed(title=cal_event.title,
                          description=cal_event.description,
                          colour=0x0E1328)
    logger.info(f"Making announcement for: {cal_event.title}, {cal_event.description}")
    await announcement_channel.send(cal_event.get_announcement())
    await announcement_channel.send(embed=embed)
