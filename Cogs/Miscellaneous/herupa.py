import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
import os

class Herupa(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='herupa',
                    description = 'Herupa will join the voice channel and say her name.',
                    brief = "Hear Herupa's name!",
                    aliases = ['h', 'hearmygirlfriendsvoice'],
                    pass_context = True)
    async def herupa(self, ctx):

        #Joining the voice chat
        try:
            channel = ctx.message.author.voice.channel
        except:
            await ctx.channel.send("You need to be in a voice channel to use this command.")
            return

        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        '''
        #Old discord.py bug bug required rejoining a voice channel in order to users to hear audio
        await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        '''

        await ctx.channel.send("Joined the voice channel!")

        #Playing herupa.mp3
        def find(name):
            #Find herupa.mp3 as long as it's in the package
            for root, dirs, files in os.walk(os.getcwd()):
                if name in files:
                    return os.path.join(root, name)

        song_there = os.path.isfile(find("herupa.mp3"))

        try:
            if song_there:
                herupa_path = find("herupa.mp3")
        except Exception as e:
            await ctx.channel.send("[Error]: herupa.mp3 is missing!")
            return

        voice = get(self.client.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(herupa_path), after=lambda e: print("Just said my name!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

def setup(client):
    client.add_cog(Herupa(client))
