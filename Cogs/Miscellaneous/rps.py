import discord
from discord.ext import commands
import random

class RPS(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name = 'rps',
                    description = 'Play rock, paper, scissors against Herupa!',
                    brief = 'Play rock, paper, scissors.')
    async def rps(self, ctx, arg):
        user_input = arg.lower()
        answer_choices = ['rock', 'paper', 'scissors']
        bot_choice = random.choice(answer_choices)

        if user_input == 'rock' and bot_choice == 'scissors':
            await ctx.channel.send('You won! I picked scissors.')
        elif user_input == 'paper' and bot_choice == 'rock':
            await ctx.channel.send('You won! I picked rock.')
        elif user_input == 'scissors' and bot_choice == 'paper':
            await ctx.channel.send('You won! I picked paper.')
        elif user_input != 'rock' and user_input != 'paper' and user_input != 'scissors':
            await ctx.channel.send('Please pick between rock, paper, or scissors.')
        elif user_input == bot_choice:
            await ctx.channel.send(f"It's a draw! We both picked {bot_choice}.")
        else:
            await ctx.channel.send(f'You lost! I picked {bot_choice}.')


def setup(client):
    client.add_cog(RPS(client))
