import builtins
from . import config
from discord.ext import commands
from . import logging
logging.init()
builtins.bot = commands.Bot(command_prefix=config.creds['prefix'])

from workshop_bot.logging import logger

@bot.event
async def on_ready():
    logger.info('Ready!')
    