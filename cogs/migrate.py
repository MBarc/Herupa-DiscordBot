import discord
from discord.ext import commands

class Migrate(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name = 'move',
                    description = 'Mass migrate people to another voice channel.',
                    brief = 'Move all members of your voice channel to another channel.')
    async def rps(self, ctx, *args):
        user_input = list(args)

        tracker = None #placeholder variable
        for word in user_input:

            if word == user_input[len(user_input) - 1]:  # if equal to the last word
                True  # do nothing
            else:
                word = word + " " #include a space afterwards since it's not the last word in the list

            if tracker == None:
                tracker = word
            else:
                tracker += word

        user_input = tracker
        for guild in self.client.guilds:
            for channel in guild.channels:
                if channel.name == user_input:
                    print(channel.name)
                    print(channel.members)

                    #Grab all voice members where the author is at
                    currentChannel = ctx.message.author.voice.channel.members
                    print(ctx.message.author.voice.channel.name)
                    print(currentChannel)

                    for member in currentChannel:
                        await member.move_to(channel)

def setup(client):
    client.add_cog(Migrate(client))
