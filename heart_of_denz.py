import discord
import random
from discord.ext import commands
import os

TOKEN = ''

client = commands.Bot(command_prefix = "d!")

@client.command(pass_context=True)
async def commands(ctx):
    await client.say('```This command shows the help dialogue box! \n The prefix is d! \n ----- The available commands are 1)goal \n ----- This shows how many minutes are left to reach the goal \n ----- 2)hi \n ----- Its simple! it says hi! \n ----- 3)spam \n ----- This command lets u spam text till a limit of 20! syntax: d!spam <text> <no. of times>```')

@client.command(pass_context=True)
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

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
    await client.say('WE HAVE 303 Minutes of watchtime, 20 Subscribers, 332 Views and 2 videos! <@%s>' % (ctx.message.author.id))





client.run(os.getenv('TOKEN'))


