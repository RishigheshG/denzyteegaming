import discord
import random
from discord.ext import commands
import os

TOKEN = ''

client = commands.Bot(command_prefix = "d!")

@client.command(pass_context=True)
async def commands(ctx):
    await client.say('```This command shows the help dialogue box! \n The prefix is d! \n ----- \n The available commands are \n ----- \n 1)goal \n ----- \n This shows how many minutes are left to reach the goal \n ----- \n 2)hi \n ----- \n Its simple! it says hi! \n ----- \n 3)spam \n ----- \n This command lets u spam text till a limit of 20! syntax: d!spam <text> <no. of times>```')

@client.command(pass_context=True)
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await client.say(rancoin)

@client.command(pass_context=True)
async def goodnight(ctx):
    await client.say("***Yay! At last you leave us alone!!***")
    
@client.command(pass_context=True)
async def magicball(ctx):
    choices = ["Most probably", "It is Imminent", "Withiut a Doubt", "Definitely", "It is possible", "Maybe" ,"Mostly", "Impossible", "No way!" , "Oh Hell NO!"]
    rancom = random.choice(choices)
    await client.say(rancom)

@client.command(pass_context=True)
async def spam(ctx):
    a = ctx.message.content
    x = a.split(" ")
    del x[0]
    b = int(x[2], base=10)
    if(b<20):
        for i in range(0,b):
            await client.say(x[1])

@client.command(pass_context=True)
async def goal(ctx):
    await client.say('WE HAVE 357 Minutes of watchtime, 20 Subscribers, 435 Views and 3 videos! <@%s>' % (ctx.message.author.id))





client.run(os.getenv('TOKEN'))


