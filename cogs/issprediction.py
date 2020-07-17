import discord
from discord.ext import commands
from lxml import html
import requests

class IssPrediction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def issprediction(self, ctx, *args):

        # Formatting input
        args = list(args) # tuples are immutable, converting to list for item assignment
        args = [word.lower() for word in args] # lowering each word
        args = [word.capitalize() for word in args] # capitalizing each word

        amountOfValues = len(args)
        needToPop = []
        # Combining multiple indexes into 1 appropriatly. Example -> Before: ("United", "States,")     After: ("United States")
        for i in range (0, amountOfValues):
            if ',' in args[i] and (',' not in args[i - 1]):

                args[i-1] = args[i - 1] + " " + args[i] # item assignment
                needToPop.append(args[i])

        # Removing any extra words from formatted args array.
        for extraWord in needToPop:
            for word in args:
                if extraWord == word:
                    args.remove(word)

        # If a city has multiple words in its name, combine those words into the same array index
        placeholder = ""
        for word in args:
            if not "," in word:
                placeholder += word + " "

        args[2] = placeholder # put the result back in the array

        for word in args: # removing any standalone words
            if "," not in word and " " not in word:
                args.remove(word)


        # Formatting words for the URL
        country = args[0].replace(",", "").replace(" ", "_")
        print(country)
        region = args[1].replace(",", "").replace(" ", "_")
        print(region)
        city = args[2].replace(",", "").replace(" ", "_")[:-1] #removes trailing space character
        print(city)

        # Getting the page
        issURL = f'https://spotthestation.nasa.gov/sightings/view.cfm?country={country}&region={region}&city={city}#.XwTMtChKiUn'
        print(issURL)
        page = requests.get(issURL)
        tree = html.fromstring(page.content)

        message = f'Here are the next 3 times the I.S.S. will be visible from {city.replace("_", " ")}: \n'

        # Extracting the info from the HTML table on the page
        startingPoint = 2
        for i in range(0,3):
            message += '» ' + tree.xpath(f'/html/body/div[2]/div[4]/div[1]/div[1]/div[6]/table/tr[{startingPoint + i}]/td[1]')[0].text_content() + '\n'

        await ctx.channel.send(message)

    @issprediction.error
    async def issprediction_error(self, ctx, error):
        error = str(error)
        if "IndexError" in error:
            await ctx.channel.send("That location is not specifically tracked for locations by N.A.S.A. Please try the closest major location to the one you requested.")

        herupaErrorLogChannel = self.client.get_channel(694819625501720606)
        await herupaErrorLogChannel.send(f"Issprediction error: {error}")

def setup(client):
    client.add_cog(IssPrediction(client))
