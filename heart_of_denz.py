import discord
from discord.ext import commands
import os

TOKEN = ''

client = commands.Bot(command_prefix = "d?")

@client.command()
async def hi():
    await client.say('Hello shanky')




client.run(os.getenv('TOKEN'))


