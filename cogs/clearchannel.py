import discord
import datetime
from discord.ext import commands, tasks


class ClearChannel(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.clearchannel.start()

    @tasks.loop(seconds=60.0)
    async def clearchannel(self):
        currentHour = datetime.datetime.now().hour
        currentMinute = datetime.datetime.now().minute

        channelsIDsToBeCleared =  [694819625501720609, 694819625501720612, 728378137129386036] # [💰money-talk💰, 💬small-talk💬, 🗣the-lobby🗣]

        if currentHour == 18 and currentMinute == 57:
            for channel in channelsIDsToBeCleared:

                channel = self.client.get_channel(channel)
                await channel.purge(limit = 200)

    @clearchannel.before_loop
    async def clearchannel_before(self):
        await self.client.wait_until_ready()

def setup(client):
    client.add_cog(ClearChannel(client))
