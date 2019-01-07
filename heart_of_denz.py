import discord
from discord.ext import commands

TOKEN = ''

client = commands.Bot(command_prefix = "d?")

@client.command()
async def hi():
    await client.say('Hello :3',client.message.author)




client.run(os.getenv('TOKEN'))


