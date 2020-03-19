import discord
from discord.ext import commands
from . import config
import workshop_bot.setup

from . import scheduler

def main():
    bot.loop.create_task(scheduler.check_schedule())
    bot.run(config.creds['discord_token'])

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)
    await announcement_channel.send("hello")
