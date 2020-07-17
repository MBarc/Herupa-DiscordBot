import discord
from discord.ext import commands
from discord.utils import get

class LennyMoney(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def newbie(self, ctx):
        if ctx.message.channel.name == "📁rules📂":

            if "I ACCEPT" in ctx.message.content.upper():

                chiliesRole = get(ctx.message.guild.roles, name='chilies')
                await ctx.message.author.add_roles(chiliesRole)
                await ctx.message.delete()

def setup(client):
    client.add_cog(LennyMoney(client))
