import discord
from discord.ext import commands
import os

TOKEN = ''

client = commands.Bot(command_prefix = "d!")

@client.command(pass_context=True)
async def commands(ctx):
    await client.say('```This command shows the help dialogue box! \n The prefix is d! \n ----- The available commands are 1)goal \n ----- This shows how many minutes are left to reach the goal \n ----- 2)hi \n ----- Its simple! it says hi! \n ----- 3)spam \n ----- This command lets u spam text till a limit of 20! syntax: d!spam <text> <no. of times>```')

@client.command(pass_context=True)
async def hi(ctx):
    await client.say('Yo Boi <@%s>' % (ctx.message.author.id))

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

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


