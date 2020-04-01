import builtins
from . import config
from discord.ext import commands
from . import logging
logging.init()
builtins.bot = commands.Bot(command_prefix=config.creds['prefix'])

from calendar_bot.logging import logger

@bot.event
async def on_ready():
    global announcement_channel, log_channel

    builtins.log_channel = bot.get_channel(config.creds['stream_log_id'])
    builtins.announcement_channel = bot.get_channel(config.creds['announcement_id'])

    logger.info('Bot Online!')
    
