import discord
import asyncio
from . import config
from . import calendar
from . import event
import workshop_bot.setup
from workshop_bot.logging import logger

async def check_schedule():
    await bot.wait_until_ready()
    # Repeat every 60 seconds
    while True:

        cal_event = calendar.check_calendar()
        if cal_event.announcement:
            await send_announcement(event)
        if cal_event.send_token:
            await send_token(event)

        await asyncio.sleep(60)

async def send_announcement(cal_event):

    announcement_channel = bot.get_channel(config.creds['announcement_id'])
    embed = discord.Embed(title=cal_event.title,
                          description=cal_event.description,
                          colour=0x0E1328)
    logger.info("Making announcement for: {}, {}".format(cal_event.title, cal_event.description))
    await announcement_channel.send(embed=embed)

async def send_token(cal_event):

    host = bot.get_guild(config.creds['guild_id']).get_member(int(cal_event.organiser_id))
    log_channel = bot.get_channel(config.creds['stream_log_id'])

    if host is None:
        logger.info(f'Unable to get user object for \'{host}\', DMing stream_log channel')
        await log_channel.send("Stream key could not be sent for event: {} at {:02d}:{:02d}".format(cal_event.title, cal_event.hour, cal_event.minute))

    embed = discord.Embed(title='Here is your Stream Key',
                          description=str(cal_event.generate_stream_key()),
                          colour=0x0E1328)

    embed.set_footer(text='Any problems, contact @wrussell1999#6267')
    await host.send(embed=embed)
    await log_channel.send("Stream key send to {}".format(host.name))
