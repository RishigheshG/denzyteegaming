import discord
from discord.ext import commands
import os

TOKEN = ''

client = commands.Bot(command_prefix = "d? " or "D? ")

@client.command(pass_context=True)
async def hi(ctx):
    await client.say('Hello shanky <@%s>',client.message.author)




client.run(os.getenv('TOKEN'))


