import discord
from discord.ext import commands
import datetime
from . import config
from . import scheduler
import calendar_bot.setup
from calendar_bot.logging import logger

def main():
    bot.loop.create_task(scheduler.check_schedule())
    scheduler.setup()
    bot.run(config.creds['discord_token'])

@bot.check
async def is_admin(ctx):
    authorised = ctx.author.id in config.creds['admin_ids']
    if not authorised:
        logger.warn(f'Unauthorised user \'{ctx.author.display_name}\' ({ctx.author.id}) tried to use command')
    return authorised

@bot.after_invoke
async def after_invoke(ctx):
    await ctx.message.delete()
