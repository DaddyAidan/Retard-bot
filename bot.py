import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')



@client.event
async def on_ready():
        print('Fuck You Stupid Bitch')



@client.event
async def on_member_join(member):
    print(f'WTF{member} STUPID BITCH')

@client.event
async def on_member_remove(member):
    print(f'Kill your self {member} its for the best')


@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms, your wifi is fucking horrible you wratched bitch')


@client.command()
async def cock(ctx):
    await ctx.send(f'fuck')

@client.command()
async def table(ctx):
    await ctx.send('https://www.youtube.com/watch?v=FcZd305VI60')

@client.command()
async def cockring(ctx):
    await ctx.send(f'Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole, Niggas in my butthole.')



@client.command()
async def woman(ctx):
    embed=discord.Embed(title="4 big guys and they bustin on my eyes",
    url = "https://pornhub.com/gay", description=":)", color=0xFF5733)
    await ctx.send(embed=embed)

@client.command()
async def embed2(ctx):
    embed=discord.Embed(title="Rains Beautiful Big Balls",
    url = "https://beastiegals.com/", description="Gay", color=0xFF5743)
    await ctx.send(embed=embed)

@client.command()
async def cocks(ctx):
    embed=discord.Embed(title="COCK",
    url = "https://cdn.mos.cms.futurecdn.net/BX7vjSt8KMtcBHyisvcSPK-1200-80.jpg", description="Warm", color=0xFF5783)
    await ctx.send(embed=embed)

@client.command()
async def commands(ctx):
    embed=discord.Embed(title="command list",
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="", color =0xFF5766)
    await ctx.send(embed=embed)

client.run('OTA0MjM0MDg5MTEwOTkwOTEy.YX4jng.gl2tWm38Qo4cLZd0vVLX0aK_m1g')
