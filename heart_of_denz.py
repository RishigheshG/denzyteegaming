import discord
from discord.ext import commands
import os

TOKEN = ''

client = commands.Bot(command_prefix = "d!")

@client.command(pass_context=True)
async def help(ctx):
    await client.say('This command shows the help dialogue box! \n The prefix is d! \n \t The available commands are 1)goal \n \t \t This shows how many minutes are left to reach the goal \n \t 2)hi \n \t \t Its simple! it says hi! \n \t 3)spam \n \t \t This command lets u spam text till a limit of 20! syntax: d!spam <text> <no. of times>')

@client.command(pass_context=True)
async def hi(ctx):
    await client.say('Yo Boi <@%s>' % (ctx.message.author.id))

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


