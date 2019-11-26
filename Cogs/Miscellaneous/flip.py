import discord
from discord.ext import commands
import random

class Flip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def flip(self, ctx, arg = None):

        answer_choices = ['heads', 'tails']
        bot_choice = random.choice(answer_choices)
        if arg == None:
            await ctx.channel.send(f'The coin landed {bot_choice}-side up!')
            return

        user_input = arg.lower()

        if user_input == bot_choice:
            await ctx.channel.send(f'{bot_choice.capitalize()}! You were right!')
        elif user_input != "heads" and user_input != 'tails':
            await ctx.channel.send('Please pick between "heads" or "tails".')
        else:
            await ctx.channel.send(f'You picked {user_input} but the coin landed on {bot_choice}-side up.')

def setup(client):
    client.add_cog(Flip(client))
