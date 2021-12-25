
import discord
from discord.ext import commands
import random

TOKEN = '' # insert your discord token here
prefix = "+"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)
client = discord.Client()


@bot.event
async def on_raw_reaction_remove(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)





# notifies you when bot starts
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'crypto-investor-bottest':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is you random number: {random.randrange(100000)}'
            await message.channel.send(response)
            return


    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return





client.run(TOKEN)
