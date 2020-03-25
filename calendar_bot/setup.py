import builtins
from . import config
from discord.ext import commands

builtins.bot = commands.Bot(command_prefix=config.creds['prefix'])
@bot.event
async def on_ready():
    print('Ready!')
    
