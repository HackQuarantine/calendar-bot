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
        current_time = now
        announcement_time = (cal_event.start - datetime.timedelta(minutes=10))
        log_time = (cal_event.start - datetime.timedelta(minutes=30))
        
        if check_times(current_time, announcement_time):
            await send_announcement(cal_event)
        elif check_times(current_time, log_time):
            await send_log(cal_event)
        await asyncio.sleep(60)

async def send_announcement(cal_event):

    announcement_channel = bot.get_channel(config.creds['announcement_id'])
    log_channel = bot.get_channel(config.creds['stream_log_id'])

    embed = discord.Embed(title=cal_event.title,
                          description=cal_event.description,
                          colour=0x0E1328)
    log_msg = f"Making announcement for: {cal_event.title}, {cal_event.description}"
    logger.info(log_msg)
    await log_channel.send(log_msg)
    await announcement_channel.send(cal_event.get_announcement())
    await announcement_channel.send(embed=embed)

async def send_log(cal_event):

    log_channel = bot.get_channel(config.creds['stream_log_id'])
    await log_channel.send(f"30 minutes until {cal_event.title}, {cal_event.description}.\n\Announcement due in 20 minutes!")

def check_times(current_time, announcement_time):
    current_year = current_time.strftime("%Y")
    current_month = current_time.strftime("%m")
    current_day = current_time.strftime("%d")
    current_hour = current_time.strftime("%H")
    current_minute = current_time.strftime("%M")
    
    announcement_year = announcement_time.strftime("%Y")
    announcement_month = announcement_time.strftime("%m")
    announcement_day = announcement_time.strftime("%d")
    announcement_hour = announcement_time.strftime("%H")
    announcement_minute = announcement_time.strftime("%M")

    if current_year == announcement_year and current_month == announcement_month and current_day == announcement_day:
        if current_hour == announcement_hour and current_minute == announcement_minute:
            return True
        else:
            return False
    else:
        return False
