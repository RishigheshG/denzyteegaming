import discord
from discord.ext import commands
import os

TOKEN = ''

client = commands.Bot(command_prefix = "d? ")

@client.command(pass_context=True)
async def hi(ctx):
    await client.say('Hello <@%s>' % (ctx.message.author.id))

@client.command(pass_context=True)
async def spam(ctx):
    a = ctx.message.content
    x = a.split(" ")
    del x[0]
    b = int(x[2], base=10)
    for i in range(0,b):
        await client.say(x[1])




client.run(os.getenv('TOKEN'))


