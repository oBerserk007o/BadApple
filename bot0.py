from os import listdir
import time
import discord
from discord.ext import commands

tokens = open("tokens.txt", "r").read()
token = tokens.split(",")[0]
directory = listdir("text_frames_with_blur")
directory.sort(key=lambda l: int(l[:-4]))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='%0', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def delay(ctx):
    starting = time.time()
    msg = open("text_frames_with_blur\\330.txt", 'r', encoding='utf-8').read()
    await ctx.send(msg)
    end = time.time()
    await ctx.send(f"Took: {end - starting} seconds")


@bot.command()
async def send(ctx, msg):
    await ctx.send(msg)


@bot.command()
async def start(ctx):
    i = 0
    s = time.time()
    while i <= 5:
        starting = time.time()
        await ctx.send(i)
        time.sleep(1 - (time.time() - starting))
    await ctx.send(f"Took {time.time() - s} seconds, was supposed to take 5")


@bot.command()
async def spamstart(ctx, member: discord.Member):
    mention = member.mention
    for i in range(100):
        await ctx.send(mention + " I'm over here stroking ma dick, i got lotion on my dick")
        time.sleep(0.2)


bot.run(token)
