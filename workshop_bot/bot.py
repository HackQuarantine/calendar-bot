import discord
from discord.ext import commands

from . import config

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Ready!')

def main():
    bot.run(config.creds['token'])
