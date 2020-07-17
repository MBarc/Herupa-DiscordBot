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

        noArgGiven = [
            f"The coin landed {bot_choice}-side up! That's my favorite side.",
            f"The coin landed {bot_choice}-side up! This wasn't rigged. . . I swear :fingers_crossed:.",
            f"The coin landed {bot_choice}-side up! Did you lose a bet?"
        ]

        userChoiceCorrect = [
            f"{bot_choice.capitalize()}! You were right!",
            f"{bot_choice.capitalize()}! Are you psychic?",
            f"Hold on the coin is still in the air . . . . . .{bot_choice.capitalize()}! Are you cheating?",
            f"Sorry but it landed {bot_choice.capitalize()}. Wait, that's what you said? Oh, congrats!"
        ]

        userChoiceWrong = [
            f"The coin landed {bot_choice}-side up. Dang it! I had money on this one :unamused:.",
            f"Did the coin just land {bot_choice}-side up or are you just happy to see me?",
            f"Do you want the bad news first? The coin landed {bot_choice}-side up!"
        ]

        if arg == None:
            await ctx.channel.send(random.choice(noArgGiven))
            return

        user_input = arg.lower()

        if user_input == bot_choice:
            await ctx.channel.send(random.choice(userChoiceCorrect))
        elif user_input != "heads" and user_input != 'tails':
            await ctx.channel.send('Please pick between "heads" or "tails".')
        else:
            await ctx.channel.send(random.choice(userChoiceWrong))

def setup(client):
    client.add_cog(Flip(client))
