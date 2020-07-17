import discord
import json
from discord.ext import commands, tasks

class AFKTracker(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.databasePath = 'C:\\path\\to\\afktracker.json'
        self.afktracker.start()

    @tasks.loop(seconds=60.0)
    async def afktracker(self):

        def write_json(data, filename=self.databasePath):
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

        halfHourVoiceChannel = self.client.get_channel(694819625917087791)
        HourVoiceChannel = self.client.get_channel(694819625917087792)
        HourAndAHalfVoiceChannel = self.client.get_channel(694819625917087793)
        thatBitchDeadVoiceChannel = self.client.get_channel(694819626378592276)
        afkNotes = self.client.get_channel(694819625917087790)

        afkExceptionChannels = ["🍿Auditorium 1🍿"]

        # Getting the data from the favorites database
        with open(self.databasePath) as json_file:
            data = json.load(json_file)

        for member in self.client.guilds[0].members:
            if member.status != discord.Status.idle:
                if data.get(member.name):
                    del data[member.name]
                    write_json(data)

            if member.status == discord.Status.idle and member.voice:
                if member.voice.channel not in afkExceptionChannels:
                    if not data.get(member.name):
                        infoToAdd = {f"{member.name}": {"count": 0}}
                        data.update(infoToAdd)
                        write_json(data)
                        await afkNotes.send(f"Started keeping track of {member.mention}'s idleness.")

                    data[member.name]['count'] += 1
                    write_json(data)

                if data.get(member.name) and (data[member.name]['count'] >= 31 and data[member.name]['count'] < 61):
                    if member.voice.channel != halfHourVoiceChannel:
                        await member.move_to(halfHourVoiceChannel)
                        await afkNotes.send(f'Moved {member.mention} to {member.voice.channel}.')

                if data.get(member.name) and (data[member.name]['count'] >= 61 and data[member.name]['count'] < 91):
                    if member.voice.channel != HourVoiceChannel:
                        await member.move_to(HourVoiceChannel)
                        await afkNotes.send(f'Moved {member.mention} to {member.voice.channel}.')

                if data.get(member.name) and (data[member.name]['count'] >= 91 and data[member.name]['count'] < 121):
                    if member.voice.channel != HourAndAHalfVoiceChannel: # id for 90 minutes voice channel
                        await member.move_to(HourAndAHalfVoiceChannel)
                        await afkNotes.send(f'Moved {member.mention} to {member.voice.channel}.')

                if data.get(member.name) and data[member.name]['count'] >= 121:
                    if member.voice.channel != thatBitchDeadVoiceChannel:
                        await member.move_to(thatBitchDeadVoiceChannel)
                        await afkNotes.send(f'Moved {member.mention} to {member.voice.channel}.')

                await afkNotes.send(f'{member.name} is at {data[member.name]["count"]}')

    @afktracker.before_loop
    async def afktracker_before(self):
        await self.client.wait_until_ready()

def setup(client):
    client.add_cog(AFKTracker(client))
