'''
Main script that holds commands.
'''

import discord
import config # in the same directory ; imports bot_prefix and token
import asyncio

client = Bot(command_prefix=config.start['bot_prefix'])

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('-------------')
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
             
@client.command(name='birthday',
                description = 'Sends member a private message wishing a happy birthday from the administrators.',
                brief = 'Sends user a PM wishing happy birthday.',
                aliases = ['bday'],
                pass_context = True)
async def birthday(context):
    author = context.message.author #grabs message author
    
    admins = [] # contains list of server admins
    for member in server.members:
      for role in member.roles:
        if role.name == 'the joestars':
          admins.append(member)
          
    await client.send_message(author, "Happy Birthday from {0}".format(admins)) # actually sends birthday message


client = MyClient()
client.run(TOKEN)
