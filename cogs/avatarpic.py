import discord
from discord.ext import commands

class AvatarPic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avatarpic(self, ctx, avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        await ctx.send(userAvatarUrl)

def setup(client):
    client.add_cog(AvatarPic(client))
