import discord
from discord.ext import commands
import pprint
import requests
import re

TOKEN = 'NTQ2NDkyNTYxMDQ1NDU0ODY4.D0pA0A.P7oXTCDd8ZNUtWxOyRlwbnZIpfI'

client = commands.Bot(command_prefix = 'z-')

@client.event
async def on_ready():
    print('Awaiting your command')
'''
@client.event
async def on_message(message):

    channel = message.channel
    
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='pray', value='Usage: z-pray (location)')
    embed.add_field(name='eat', value='Usage: z-eat (all | (food)) (location)')

    if message.content == 'z-help':
        await client.send_message(channel, '```Commands:\nz-pray ( location ) -- shows you the closet available praying location\nz-eat ( all | [foodtype] ) ( location ) -- shows you the closest available eating location with a specific food```')
'''
@client.command()
async def pray(*args):
    output = ''
    for word in args:
        output += word

    url = 'http://iphone.halalfire.com/bot_prayerspace.php?l={}&uuid=1&key=O2A8Uo5ACzEXW7NnPYPX'.format(output)
    res = requests.get(url)
    data = res.json()

    number = data['data']['number']
    if number == 0:
        await client.say(":x:  No nearby praying locations near {}.".format(output))

    status_text = data['data']['status_text']
    photo = data['data']['photo_url']
    name = data['data']['name']
    placetype = data['data']['type']
    address = data['data']['address']
    city = data['data']['city']
    state = data['data']['state']
    zipcode = data['data']['zip']
    phone = data['data']['phone']
    distance = data['data']['distance']
    desc = data['data']['desc']
    zabihah_url = data['data']['url']

    if number == 1:
        await client.say(':white_check_mark:  Found a place to pray near {} {}:'.format(city, state))
        
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.add_field(name='Brought to you by ZabihahBot', value='{} {}'.format(desc, distance), inline=True)
    embed.add_field(name=name,value='{}\n{} {} {} \n{}'.format(address, city, state, zipcode, phone),inline=False)

    embed.set_footer(text='Click on the link for more info')
    embed.set_image(url=photo)
    embed.set_thumbnail(url='https://www.zabihah.com/img/logo_zabihah_bot.png')

    await client.say(embed=embed)
    await client.say(zabihah_url)

@client.command()
async def eat(*args):
    output = ''
    for word in args:
        output+=word
        output+=' '
    
    output2=tuple(output.split(' near '))
        
    output3 = []
    for word in output2:
        output3.append(word)

    output3.append(output3[0])
    del output3[0]

    if output[1] == '':
        output[1] = 'all'

    if output[1] != '':
        print('Searching...')
        url = 'http://iphone.halalfire.com/bot_restaurant.php?uuid=1&key=O2A8Uo5ACzEXW7NnPYPX&l={}&k={}'.format(output3[0],output3[1])
    else:
        await client.say(':x:  Not enough arguments were given.\n**USAGE** - z-eat [food] near [location]\n')

    res = requests.get(url)
    data = res.json()
    number = data['data']['number']

    if number == 0:
        await client.say(':x:  No nearby places with {}.\n**USAGE** - z-eat [food] near [location]\n'.format(output3[1]))

        
    status_text = data['data']['status_text']
    photo = data['data']['photo_url']
    name = data['data']['name']
    address = data['data']['address']
    city = data['data']['city']
    state = data['data']['state']
    zipcode = data['data']['zip']
    phone = data['data']['phone']
    distance = data['data']['distance']
    desc = data['data']['desc']
    tags = data['data']['tags']
    zabihah_url = data['data']['url']
    keyword = data['data']['keyword']

    if number == 1:
        await client.say(':white_check_mark:  Found a place to eat{}near {} {}:'.format(keyword, city, state))
        
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.add_field(name='{}'.format(status_text), value="{} {}".format(desc, distance), inline=True)
    embed.add_field(name=name,value='{}\n{}\n{} {} {} \n{}'.format(tags, address, city, state, zipcode, phone),inline=False)
    embed.set_footer(text='Click on the link below for more info'.format(zabihah_url))
    embed.set_image(url=photo)

    await client.say(embed=embed)
    await client.say(zabihah_url)
    
@client.command()
async def setchannel(*args):
    channel = ''
    for word in args:
        channel += word

    await client.say(channel)

    await client.send_message(author.server.channels, name=str(channel), content=':white_check_mark:')
    
client.run(TOKEN)
