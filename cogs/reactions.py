import discord
from discord.ext import commands
from discord.utils import get

class Reactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        channel = await self.client.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = payload.member
        emoji = payload.emoji

        if message.id == 727219710428708947: # self assign setup message
            if str(emoji) == '0️⃣':
                animalCrossingRole = get(member.guild.roles, name='animal crossing')
                await member.add_roles(animalCrossingRole)

            if str(emoji) == '1️⃣':
                callOfDutyRole = get(member.guild.roles, name='call of duty')
                await member.add_roles(callOfDutyRole)

            if str(emoji) == '2️⃣':
                destinyRole = get(member.guild.roles, name='destiny')
                await member.add_roles(destinyRole)

            if str(emoji) == '3️⃣':
                fortniteRole = get(member.guild.roles, name='fortnite')
                await member.add_roles(fortniteRole)

            if str(emoji) == '4️⃣':
                overwatchRole = get(member.guild.roles, name='overwatch')
                await member.add_roles(overwatchRole)

            if str(emoji) == '5️⃣':
                rainbow6Role = get(member.guild.roles, name='rainbow 6')
                await member.add_roles(rainbow6Role)

            if str(emoji) == '6️⃣':
                rocketLeagueRole = get(member.guild.roles, name='rocket league')
                await member.add_roles(rocketLeagueRole)

            if str(emoji) == '7️⃣':
                sims4Role = get(member.guild.roles, name='sims 4')
                await member.add_roles(sims4Role)

            if str(emoji) == '8️⃣':
                spaceBuddiesRole = get(member.guild.roles, name='space buddies')
                await member.add_roles(spaceBuddiesRole)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        print("emoji removed!")

        guild = self.client.get_guild(payload.guild_id)
        channel = await self.client.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = guild.get_member(payload.user_id)
        emoji = payload.emoji
        print('removed emoji', str(emoji) )

        if message.id == 727219710428708947:  # self assign setup message

            print('made it in the if statement')
            if str(emoji) == '0️⃣':
                animalCrossingRole = get(member.guild.roles, name='animal crossing')
                await member.remove_roles(animalCrossingRole)

            if str(emoji) == '1️⃣':
                callOfDutyRole = get(member.guild.roles, name='call of duty')
                await member.remove_roles(callOfDutyRole)

            if str(emoji) == '2️⃣':
                destinyRole = get(member.guild.roles, name='destiny')
                await member.remove_roles(destinyRole)

            if str(emoji) == '3️⃣':
                fortniteRole = get(member.guild.roles, name='fortnite')
                await member.remove_roles(fortniteRole)

            if str(emoji) == '4️⃣':
                overwatchRole = get(member.guild.roles, name='overwatch')
                await member.remove_roles(overwatchRole)

            if str(emoji) == '5️⃣':
                rainbow6Role = get(member.guild.roles, name='rainbow 6')
                await member.remove_roles(rainbow6Role)

            if str(emoji) == '6️⃣':
                rocketLeagueRole = get(member.guild.roles, name='rocket league')
                await member.remove_roles(rocketLeagueRole)

            if str(emoji) == '7️⃣':
                sims4Role = get(member.guild.roles, name='sims 4')
                await member.remove_roles(sims4Role)

            if str(emoji) == '8️⃣':
                spaceBuddiesRole = get(member.guild.roles, name='space buddies')
                await member.remove_roles(spaceBuddiesRole)

def setup(client):
    client.add_cog(Reactions(client))
