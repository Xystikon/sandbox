import discord
from discord.ext import commands

TOKEN = 'NTQzOTUzNDM2NTUxNDEzNzcw.D0EFWQ.koaPnK_GT59KJtfKqP4Xis2CqKI'

client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
    print('')

client.run(TOKEN)
