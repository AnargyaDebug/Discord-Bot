import discord
from discord.ext import commands
from bot_logic import random_word
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=";", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def bye(ctx):
    await ctx.send("B-bye")

@bot.command()
async def what(ctx):
    await ctx.send("I'm a chatbot!")

@bot.command()
async def why(ctx):
    await ctx.send("I'm just a test subject :(")

@bot.command()
async def commands(ctx):
    await ctx.send("Commands are: ;halo, ;bye, ;what, ;why, ;flip-coin, ;gibberish, ;pop <amount>")

@bot.command()
async def flipcoin(ctx):
    rand = random.randint(0, 1)
    result = "Heads" if rand == 0 else "Tails"
    await ctx.send(result)

@bot.command()
async def gibberish(ctx, length=10):
    length = 4000 if length > 4000 else length
    gibberish_list = [random_word(length), random_word(length), random_word(length), random_word(length), "E", "🦍"]
    result = random.choice(gibberish_list)
    await ctx.send(result)

    if result == "E":
        await ctx.send("YOU HAVE ENCOUNTERED E")
    elif result == "🦍":
        await ctx.send("YOU HAVE ENCOUNTERED THE GORILLA")

bot.run("MTEzODgxMzA1NDUzMjk5NzIzMg.GGhian.heTG_r2P2rQ_UDfC1gFkCzBHV1JtHhqP8Xn--Q")
