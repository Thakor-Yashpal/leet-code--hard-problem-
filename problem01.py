import discord
from discord.ext import commands

# Replace TOKEN with your bot's token
TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Create a Discord client
client = commands.Bot(command_prefix='!')

# Event that runs when the bot is ready
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Event that runs when a message is received
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Respond to the "!hello" command
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# Run the bot with the specified token
client.run(TOKEN)
