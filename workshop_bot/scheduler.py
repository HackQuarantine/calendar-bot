import discord
import asyncio
from . import config
from . import calendar
import workshop_bot.setup

async def check_schedule():
    await bot.wait_until_ready()
    # Repeat every 60 seconds
    while True:

        title, description = calendar.check_calendar()
        await send_announcement(title, description)

        await asyncio.sleep(60)

async def send_announcement(title, description):

    announcement_channel = bot.get_channel(config.creds['announcement_id'])
    embed = discord.Embed(title=title,
                          description=description,
                          colour=0x0E1328)
    print("Making announcement for: {}, {}".format(title, description))
    await announcement_channel.send(embed=embed)