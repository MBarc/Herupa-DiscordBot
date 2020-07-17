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
                    aliases = ['h', 'hearmygirlfriendsvoice'])
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
            await channel.connect()
            await ctx.channel.send("Joined the voice channel!")

        def find(name):
            #Find {name}.mp3 within the 'herupa names' directory
            for root, dirs, files in os.walk(os.getcwd() + "\\cogs\\herupa names"):
                if name in files:
                    return os.path.join(root, name)

        name = ctx.message.content.split()[1]
        song_there = os.path.isfile(find(name + ".mp3"))

        try:
            if song_there:
                name_path = find(name + ".mp3")
        except:
            await ctx.channel.send(f"[Error]: {name} is not a name I'm familiar with, tell @Money Shark#0643 to teach me more names.")
            return

        voice = get(self.client.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(name_path))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.90

    @herupa.error
    async def herupa_error(self, ctx, error):
        error = str(error)
        if "TypeError: stat: path should be string, bytes, os.PathLike or integer, not NoneType" in error:
            moneyshark = '<@400475368550694942>'
            await ctx.channel.send(f"Hello there! Sorry I don't know how to pronounce that name. Please let {moneyshark} know (he's my english teacher).")

        herupaErrorLogChannel = self.client.get_channel(694819625501720606)
        await herupaErrorLogChannel.send(f"Herupa command error: {error}")

def setup(client):
    client.add_cog(Herupa(client))
