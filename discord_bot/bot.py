import discord
from discord.ext import commands
import pprint
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=Fairfax,us&appid=ac7c75b9937a495021393024d0a90c44'
res = requests.get(url)
data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']
description = data['weather'][0]['description']

ftemp = 'Temperature : {} Degrees Kelvin'.format(temp)
fwind = 'Wind Speed : {} m/s'.format(wind_speed)
fdesc = 'Description : {}'.format(description)

TOKEN = 'NTQzOTUzNDM2NTUxNDEzNzcw.D0EFWQ.koaPnK_GT59KJtfKqP4Xis2CqKI'

client = commands.Bot(command_prefix = 's/')


@client.event
async def on_ready():
    print('Awaiting your command')

@client.command()
async def ping():
    await client.say('Pong')

@client.command()
async def weather():
    await client.say(ftemp+'\n'+fwind+'\n'+fdesc)
    
@client.command()
async def wind():
    await client.say(fwind)

@client.command()
async def desc():
    await client.say(fdesc)

@client.command()
async def temp():
    await client.say(ftemp)

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
