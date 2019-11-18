'''
Main script that holds commands.
'''

import discord
import config # in the same directory ; imports bot_prefix and token
import asyncio
import datetime # for birthday commmand
import json # for databases
import random #for member of the week and coin flip

from discord.ext.commands import Bot

client = Bot(command_prefix=config.start['bot_prefix'])

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('-------------')
  await member_of_the_week()
  await birthday_background()
             
@client.command(name='herupa',
                description = 'Herupa will join the voice channel that the user in and say her name.',
                brief = "Hear Herupa's voice.",
                pass_context = True)
async def herupa(context):
    print("Herupa command executed by %s." % context.message.author.name)
    # grab the user who sent the command
    user = context.message.author
    voice_channel = user.voice.voice_channel
    channel = None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel = voice_channel.name
        await client.say('User is in channel: '+ channel)
        # create StreamPlayer
        vc = await client.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('herupa.mp3')
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        player.stop()
        await vc.disconnect()
    else:
        await client.say('User is not in a channel.')
    
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
            
async def member_of_the_week():
  print("Started Member of the Week function!")
  for server in client.guilds:

    #Checks to see if the user is an admin, bot, or regular member
    members = []
    admins = []
    for member in server.members:
      if member.bot: 
        pass #does not add bot to members list
      else:
        for role in member.roles:
          if role.name == 'the joestars':
            admins.append(member)

        members.append(member.name)

    #Removes admin from members list
    members = (set(members) - set(admins))

    for channel in server.channels:
      if channel.name == '\U0001f38amember-of-the-week\U0001f38a':

        try:
          pins = await discord.abc.Messageable.pins(channel)
          last_pin = pins[-1].created_at.now()
          when_message_sent = datetime.date(last_pin.year, last_pin.month, last_pin.day).isocalendar()[1]
        except Exception as e:
          when_message_sent = 57 # current week will never be equal to this ; only 56 weeks in a year

        current_date = datetime.datetime.now()
        current_week = datetime.date(current_date.year, current_date.month, current_date.day).isocalendar()[1]
      
        if when_message_sent == current_week:
          pass
        else:
          bot_message = await channel.send("Congratulations to %s on being this week's Member of the Week! We appreciate ya!" % str(random.choice(members).mention))

          pin_bot_message = await bot_message.pin()
          
@client.command(name='clear',
                description = 'Allows user to delete messages in bulk.',
                brief = 'Allows user to delete messages in bulk.',
                pass_context = True)
async def clear(ctx, amount = 5):
  if ctx.message.author.permissions.manage_messages:
    await ctx.channel.purge(limit = amount + 1) # +1 to delete the original command that triggered this function
  else:
    await ctx.channel.send("You do not have permissions to manage messages.") 
    
@client.command(name='flip',
                description = 'Flips a coin.',
                brief = 'Flips a coin.',
                aliases = ['coinflip'],
                pass_context = True)
async def flip(ctx):
  user_input = ctx.message.content
  answer_choices = ['heads', 'tails']
  bot_choice = random.choice(answer_choices)
  if bot_choice == "heads" and user_input.lower() == bot_choice:
    await ctx.channel.send("Heads! You were right!")
  elif bot_choice == "tails" and user_input.lower() == bot_choice:
    await ctx.channel.send("Tails! You were right!")
  elif user_input.lower() != "heads" and user_input.lower() != "tails":
    await ctx.channel.send('Please pick between "heads" or "tails".')
  else:
    await ctx.channel.send("You picked %s but the coin landed on %s" % (user_input, bot_choice)
                           
@client.command(name='rps',
                description = 'User plays "rock, paper, scissors" against the bot.',
                brief = 'Play "rock, paper, scissors".',
                pass_context = True)
async def rps(ctx):
  user_input = ctx.author.message.content
  answer_choices = ['rock', 'paper', 'scissors']
  bot_choice = random.choice(answer_choices)
                           
  if user_input.lower() == 'rock' and bot_choice == 'scissors':
    await ctx.channel.send('You won! I picked scissors.')
  elif user_input.lower() == 'paper' and bot_choice == 'rock':
    await ctx.channel.send('You won! I picked rock.')
  elif user_input.lower() == 'scissors' and bot_choice == 'paper':
    await ctx.channel.send('You won! I picked paper.')
  elif user_input.lower() == bot_choice:
    await ctx.channel.send("It's a draw! We both picked %s." % bot_choice) 
  else:
    await ctx.channel.send("You lost! I picked %s." % bot_choice)
                           
@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name = settings['channels']['default_role'])
  await client.add_roles(member, role)
  
  welcome_messages = ["Welcome %s! We're happy to have you here!",
                      "Watch out people! %s just joined the server!",
                      "Hey %s! Thanks for joining!",
                      "Enjoy your stay %s!",
                      "We got a live one! %s just joined the server!",
                      "Congrats to %s for making the amazing descision to join this server!",
                      "Oh hey, %s! It's about time you joined the server!",
                      "It's a bird, it's a plane, it's %s! Welcome to the server!",
                      "Ladies and Gentlemen of the server, please put your hands together and welcome %s!",
                      "If I had a dollar for every time %s joined the server, I'd have one dollar! Welcome!",
                      "Welcome to the server %s! We were just talking about you!",
                      "Welcome to the server, %s! Please wipe your shoes on the way in.",
                      "HEY EVERYONE! %s FINALLY JOINED THE SERVER!",
                      "Welcome to the server, %s! Make yourself at home!",
                      "Welcome to the server, %s! We hope you don't regret this. . ."]
                           
  message_choice = random.choice(welcome_messages) % member.name.mention                      
                           
  general_chat = settings['channels']['general_chat_id']
                           
  await client.send(general_chat, message_choice)
                           
@client.event
async def on_member_remove(member):

  goodbye_messages = ["%s just left the server! :(",
                      "Leaving already, %s? We were just getting started!",
                      "%s just left and we'll never be the same",
                      "And for my next trick, POOF, %s has left the server!",
                      "%s left the server and I've been in therapy ever since.",
                      "%s just left the server to go get some milk! I'm sure they'll be right back!",
                      "It's been so long since someone left, glad you guys are enjoying the server! Oh. . . actually . . . %s just left the server. That's embarrassing.",
                      "%s just left the server. Thank you for your sacrifice!"]
                           
   message_choice = random.choice(goodbye_message) % member.name.mention
                           
   general_chat = settings['channels']['general_chat_id']
                           
   await client.send(general_chat, message_choice)
      
   
                      
                             
client.run(config.auth['TOKEN'])
