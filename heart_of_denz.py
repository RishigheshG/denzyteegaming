import discord
import random
from discord.ext import commands
import os

TOKEN = ''

client = commands.Bot(command_prefix = "d!")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='with your life!'))

@client.command(pass_context=True)
async def commands(ctx):
    await client.say('```This command shows the help dialogue box! \n The prefix is d! \n ----- \n The available commands are \n ----- \n 1)goal \n -- \n This shows how many minutes are left to reach the goal \n ----- \n 2)goodnight \n -- \n Well, you should try using the command to know what it does, should\'nt you? \n ----- \n 3)spam \n -- \n This command lets u spam text till a limit of 20! syntax: d!spam <text> <no. of times> \n ----- \n 4)coinflip \n -- \n Flips a coin for you \n ----- \n 5)magicball \n -- \n Ask a question and it tells you the chances of that happening! \n ----- \n 6)clear \n -- \n This commands clears the last 100 messages by default. Unless you put the number of messages (should be less than 100) next to the command \n ----- \n 7)Denzytee \n -- \n This will give you the links to our youtube , twitter, twitch and instagram ```')

@client.command(pass_context=True)
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await client.say(rancoin)

@client.command(pass_context=True)
async def goodnight(ctx):
    await client.say("***Yay! At last you leave us alone!!*** <@%s>" % (ctx.message.author.id))

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
    b = int(x[1], base=10)
    if(b<101):
        for i in range(0,b):
            await client.say(x[0])
        
@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted.')

@client.command(pass_context=True)
async def goal(ctx):
    await client.say('Our goal is to get 240000 minutes of watchtime and 1000 subscribers! \n As of now, We Have 1930 Minutes of watchtime, 36 Subscribers, 1112 Views and 6 videos! <@%s>' % (ctx.message.author.id))

@client.command(pass_context=True)
async def denzytee(ctx):
    await client.say('Youtube: https://www.youtube.com/channel/UCGZPDIh0EIn4Rn8jdf6gSDA \n Instagram: (https://www.instagram.com/denzytee_gaming/?hl=en) \n Twitter: (https://twitter.com/DenzyteeG) \n Twitch: (https://www.twitch.tv/denzytee)')

@client.command(pass_context=True)
async def ping(ctx):
    await client.say('IM NOT JOBLESS LIKE U Dumbass !')

@client.command(pass_context=True)
async def csc(ctx):
    x=random(5)
    await asyncio.sleep(x)
    await client.say('d!na')

@client.command(pass_context=True)
async def na(ctx):
    choices = ["!play https://www.youtube.com/watch?v=U06jlgpMtQs" , "!play https://www.youtube.com/watch?v=kRPGPAnPNa8" , "!play https://www.youtube.com/watch?v=HtMF973tXIY" , "!play https://www.youtube.com/watch?v=UctriMuXYS0" , "!play https://www.youtube.com/watch?v=29FFHC2D12Q"]
    rancoin = random.choice(choices)
    await client.say(rancoin)

@client.command(pass_context=True)
async def denzplay(ctx):
    choices = ["https://www.youtube.com/watch?v=bALkuRXW144&t" , "https://www.youtube.com/watch?v=2X6sPcWEvHI&t" , "https://www.youtube.com/watch?v=ALd5myhEYIY" , "https://www.youtube.com/watch?v=ThVUcoMOs-E" , "https://www.youtube.com/watch?v=09x0q9kzxjo&t" , "https://www.youtube.com/watch?v=02fr15TZ-M8"]
    rancoin = random.choice(choices)
    await client.say(rancoin)

@client.command(pass_context=True)
async def cringe(ctx):
    await client.say('https://drive.google.com/file/d/1B0n6_rOoxrBFS4VzQYcbWW7ZrVwoDFEy/view?usp=sharing')


client.run(os.getenv('TOKEN'))


