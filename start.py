import discord
from discord.ext import commands
import os

import config #same hirearchy

client = commands.Bot(command_prefix = config.start['bot_prefix'])

@client.command()
async def load(ctx, extension):
    print(f'Loaded up {extension}!')
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for root, dirs, files in os.walk("./Cogs", topdown=False):
    for name in files:

        extension_path = os.path.join(root, name)
        extension_path = extension_path.replace('/','.').replace('\\','.')[2:-3] # package format for load_extension()

        if name.endswith(".py"):
            print(name)
            client.load_extension(extension_path)

client.run(config.auth['TOKEN'])
