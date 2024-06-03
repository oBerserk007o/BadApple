from os import listdir
import time
import discord
from discord.ext import commands

tokens = open("tokens.txt", "r").read()
token = tokens.split(",")[8]
directory = listdir("text_frames_with_blur")
directory.sort(key=lambda l: int(l[:-4]))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='%0', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def shervin(ctx):
    await ctx.send(file=discord.File('wide shervin.png'))


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
    for filename in directory:
        await send(ctx, open(f"text_frames_with_blur\\{filename}", "r", encoding='utf-8').read())
        time.sleep(1 / 5)


bot.run(token)
