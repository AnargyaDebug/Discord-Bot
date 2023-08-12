import discord
from bot_logic import gen_pass
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("$what"):
        await message.channel.send("I am a chatbot!")
    elif message.content.startswith("$why"):
        await message.channel.send("I am just a test subject :(")
    elif message.content.startswith("$commands"):
        await message.channel.send("Commands are: $halo, $bye, $what, $why, $flip-coin")
    elif message.content.startswith("$flip-coin"):
        rand = random.randint(0, 1)
        result = "Heads" if rand == 0 else "Tails"
        await message.channel.send(result)
    else:
        await message.channel.send(message.content)

client.run("MTEzODgxMzA1NDUzMjk5NzIzMg.GGhian.heTG_r2P2rQ_UDfC1gFkCzBHV1JtHhqP8Xn--Q")
