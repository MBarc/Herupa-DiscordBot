'''
This command is to make sure that people aren't using voice-dedicated
text channels as general purpose chats.
'''
import discord
import asyncio
from discord.ext import commands

class ChatModerator(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        channels = {
            "💰money-talk💰": {
                "textChannelID": 693896278425337936,
                "voiceChannelID": 648346006890610689
            },
            "💬small-talk💬": {
                "textChannelID": 693896339473301545,
                "voiceChannelID": 691321554432294942
            }
        }

        if message.channel.name in channels:

            #Checking to see if anyone is in the voice channel
            voiceChannelID = channels.get(message.channel.name)['voiceChannelID']
            voice_channel = self.client.get_channel(voiceChannelID)
            members = voice_channel.members

            #If there are no members in the voice channel, delete the message.
            if not members and not message.author.bot:
                await message.delete()
                botMessage = await message.channel.send(f"In order to to avoid people using {message.channel.name} as a general chat, messages can only be sent while someone (doesn't matter who) is in the respective voice channel. This message will now self-destruct. . .")
                await asyncio.sleep(15)
                await botMessage.delete()

def setup(client):
    client.add_cog(ChatModerator(client))
