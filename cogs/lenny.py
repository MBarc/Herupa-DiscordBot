import discord
from discord.ext import commands

class Lenny(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lenny(self, ctx):
        await ctx.message.channel.send('( ͡° ͜ʖ ͡°)')

def setup(client):
    client.add_cog(Lenny(client))
