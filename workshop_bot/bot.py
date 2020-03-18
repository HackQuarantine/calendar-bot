import discord
from discord.ext import commands

from . import config

bot = commands.Bot(command_prefix='?')

def main():
    bot.run(config.creds['token'])

@bot.event
async def on_ready():
    print('Ready!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)
    await message.channel.send("No, fuck off")
