import discord
from discord.ext import commands
import os

TOKEN = ''

client = commands.Bot(command_prefix = "d? " or "D? " or "?D" or "?d")

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


