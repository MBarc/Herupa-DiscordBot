'''
Main script that holds commands.
'''

import discord
import config # in the same directory ; imports bot_prefix and token
import asyncio
import datetime # for birthday commmand
import json # for databases
import pprint

from discord.ext.commands import Bot

client = Bot(command_prefix=config.start['bot_prefix'])

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('-------------')
  await birthday_background()
             
@client.command(name='birthday',
                description = 'Sends member a private message wishing a happy birthday from the administrators. Format is MMDD.',
                brief = 'Sends user a PM wishing happy birthday.',
                aliases = ['bday'],
                pass_context = True)
async def birthday(context, args):
    print("Birthday command executed by %s " % context.message.author.name)
    author = str(context.message.author)
    author_id = str(context.message.author.id)
    birthday = {}
    birthday[author] = []

    birth_day = int(args[2:])
    birth_month = int(args[:2])

    if birth_month >= 1 and birth_month <= 12:
      pass

    else:
      await context.message.channel.send("First two digits did not represent a month. Please use a number 01-12.")
      return


    if birth_day >= 1 and birth_day <= 31:
      pass
    
    else:
      await context.message.channel.send("Last two digits did not represent a day. Please use a number 01-31.")
      return
      
    birthday[author].append({
      'name': author,
      'id': author_id,
      'birth_day': birth_day,
      'birth_month': birth_month})

    with open('birthdaydatabase.txt', 'a') as outfile:
      outfile.write("\n") # dataset in birthday_background() needs this here
      outfile.write(json.dumps(birthday, indent=4, sort_keys=True))

async def birthday_background():
  time = datetime.datetime.now()
  #Getting list of admins for birthday message
  admins = []
  for server in client.guilds: #for every server
    for member in server.members: # go through all the members
      for role in member.roles: #check all of their roles
        if role.name == 'the joestars': #if their role is 'the joestars'
          admins.append(str(member.name)) #then add them to the admin list 

  #Checking to see whose birthday it is
  for server in client.guilds:
    for member in server.members:

      with open("birthdaydatabase.txt") as birthday_database:

        dataset = json.loads("[" + birthday_database.read().replace("}\n{", "},\n{") + "]")

        for i in range(len(dataset)): #go through each dataset
          try:
            for person in dataset[i][str(member)]:

              birth_day = int(person['birth_day'])
              birth_month = int(person['birth_month'])

              if birth_day == time.day and birth_month == time.month:
                await member.send("Happy birthday from " + ', '.join(admins[:-1]) + " and " + admins[-1] + "!!") # actually sends birthday message
                print("Just sent %s a birthday message!" % str(member))

          except Exception as e:
            #print(str(e))
            continue

client.run(config.auth['TOKEN'])
