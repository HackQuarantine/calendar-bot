import discord
from discord.ext import commands
import datetime
from . import config
import workshop_bot.setup
from . import scheduler

def main():
    bot.loop.create_task(scheduler.check_schedule())
    bot.run(config.creds['discord_token'])
