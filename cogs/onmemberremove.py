import discord
from discord.ext import commands
import json

class OnMemberRemove(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.databasePath = 'C:\\Users\\micha\\Desktop\\Chill Club Discord\\Herupa\\cogs\\databases\\favorites.json'

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        checkList = ["Remove From All Databases"] #things to do after someone has left the server

        for task in checkList:
            if task == "Remove From All Databases":

                # function to add to JSON
                def write_json(data, filepath):
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=4)

                #Removing {member}'s key/section in the database
                with open(self.databasePath) as json_file:
                    data = json.load(json_file)

                    try:
                        for name in data:
                            if name == str(member):
                                data.pop(name) # error: dictionary changed size during iteration
                    except:
                        pass

                    write_json(data, self.databasePath)

                #Removing {member} from everyone's favorites list
                with open(self.databasePath) as json_file:
                    data = json.load(json_file)

                    for individual in data:
                        individualsFavorites = data[individual]
                        for favorite in individualsFavorites:
                            if favorite == str(member):
                                data[individual] = [favorite for favorite in individualsFavorites if favorite != str(member)]

                    write_json(data, self.databasePath)

def setup(client):
    client.add_cog(OnMemberRemove(client))
