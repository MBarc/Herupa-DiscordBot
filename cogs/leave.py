import discord
from discord.ext import commands

class Leave(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='leave',
                    description = 'Makes Herupa leaves the voice chat.',
                    pass_context = True)
    async def leave(self, ctx):

        voice_client = ctx.guild.voice_client
        await voice_client.disconnect()

def setup(client):
    client.add_cog(Leave(client))
