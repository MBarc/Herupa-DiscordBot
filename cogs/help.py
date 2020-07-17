import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(
            colour = discord.Colour.from_rgb(255, 183, 197)
        )

        embed.set_author(name="Herupa's Help Page")
        embed.add_field(name='avatarpic {@member}', value='Herupa will respond with the avatar pic of the member mentioned.', inline=False)
        embed.add_field(name='clear {number}', value='Delete messages in bulk. If no number is specified, 5 messages are cleared.', inline=False)
        embed.add_field(name='flip {heads or tails}', value='Have Herupa flip a coin. Specifying heads or tails is optional.', inline=False)
        embed.add_field(name='herupa {name}', value='Herupa will join the voice channel and say the name specified.', inline=False)
        embed.add_field(name='leave', value='Tell Herupa to leave the voice channel.', inline=False)
        embed.add_field(name='lenny', value='Herupa responds with ( ͡° ͜ʖ ͡°)', inline=False)
        embed.add_field(name='lennymoney', value='Herupa responds with [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]', inline=False)
        embed.add_field(name='migrate {channel name}', value='Move everyone in your current voice channel to another voice channel.', inline=False)
        embed.add_field(name='rps', value='Play rock, paper, scissors against Herupa.', inline=False)
        embed.add_field(name='github', value="Responds with a link to Herupa's Github page", inline=False)
        embed.add_field(name='isslocation', value='Get the coordinates and map of where the International Space Station currently is.', inline=False)
        embed.add_field(name='whoisinspace', value='Get the amount and names of astronauts currently in space.', inline=False)
        embed.add_field(name='issprediction {country, region, city}', value='Get the amount and names of astronauts currently in space.', inline=False)
        embed.add_field(name='addfavorite', value='Add another member to your favorites. They must add you back in order to receives notifications of when each other joins a voice channel.', inline=False)
        embed.add_field(name='removefavorite', value='Remove another member from your favorites.', inline=False)
        embed.add_field(name='\u200b', value='\u200b')
        embed.add_field(name='--------------------------------------Background Tasks--------------------------------------', value='\u200b', inline=False)
        embed.add_field(name='AFK', value='Herupa automatically keeps track of how long members are AFK and moves them to the appropriate AFK voice channels.', inline=False)
        embed.add_field(name='Newbie', value='Responsible for assigning the newbie role to new members and assigning the chillies role once members accept to our ToS.', inline=False)
        embed.add_field(name='Clear Channel', value='Clears out certain text channels everyday at 6:30am EST.', inline=False)
        embed.add_field(name='On Member Join', value='Greets new members with a unique greeting.', inline=False)
        embed.add_field(name='Favorites', value="Sends a notification to all of your favorites (assuming you're their favorite too) letting them know that you connected to a voice chat.")
        embed.add_field(name='\u200b', value='\u200b')
        embed.set_footer(text='https://github.com/MBarc/Herupa-DiscordBot')

        await ctx.send(ctx.channel, embed=embed)

def setup(client):
    client.add_cog(Help(client))
