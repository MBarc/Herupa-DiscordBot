import discord
from discord.ext import commands

class ISSLive(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def isslive(self, ctx):
        issLivestreamURL = 'https://www.youtube.com/watch?v=EEIk7gwjgIM'
        await ctx.message.channel.send(f"Here's the link to watch the I.S.S. live: <{issLivestreamURL}>")

def setup(client):
    client.add_cog(ISSLive(client))
