import discord
from discord.ext import commands

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name='clear',
                    description = 'Allows user to delete messages in bulk.',
                    brief = 'Allows user to delete messages in bulk.',
                    pass_context = True)
    async def clear(self, ctx, amount = 5):
        try:
            if ctx.message.author.guild_permissions.manage_messages:
                await ctx.channel.purge(limit = amount + 1) # +1 to delete the original command that triggered this function
            else:
                await ctx.channel.send("You do not have permissions to manage messages.")

        except Exception as e:
            if e.code == 50013: #Missing permissions error Code
                await ctx.channel.send("I do not have permission to delete those messages on your behalf. Please allow me to manage messages.")
            else:
                await ctx.channel.send("Please report this error as an issue on the Herupa Github page: ", str(e))


def setup(client):
    client.add_cog(Clear(client))
