'''
This file will keep track of static settings for Herupa.
'''

#Link to have bot join server: https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot


# This information can  be found on the developer page.
auth = dict(
  TOKEN = 'NjQzNTYyODUyNzQxMDIxNzA3.XcnSyQ.jwx7jpeMCYJ5HyVPbvaz-h4lR9U',
  CLIENT_ID = 643562852741021707, 
  CLIENT_SECRET = 'CLRRylP7WdLww6xJZLeL8zobAtR8_1uV'
  )
  
start = dict(
  bot_prefix = "$"
  )

#You can leave a setting blank if applicable
settings = dict(
    roles = dict(
        admin = 'the joestars', #The name of the server admins
        genral_public =  'the bois', #The name of the role given to every member
        bot_role = 'ACTUAL FUCKING SLAVES'# The name of the role given to bots
        ),
    channels = dict(
        general_chat_id = 639251696635346965, #ID of the general chat
        motw_channel = '\U0001f38amember-of-the-week\U0001f38a', #The name of the Member of the Week channel
        reddit_channel = '', #Channel where reddit post are sent,
        herupa_channel = '', #Herupa's main text channel
        moderation_channel = '' #Channel where moderation posts get sent to
        )
        
    )
