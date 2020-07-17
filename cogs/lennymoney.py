import discord
from discord.ext import commands

class LennyMoney(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lennymoney(self, ctx):
        await ctx.message.channel.send('[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]')

def setup(client):
    client.add_cog(LennyMoney(client))
