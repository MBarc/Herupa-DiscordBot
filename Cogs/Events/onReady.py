import discord
from discord.ext import commands
import random, datetime
class OnReady(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in as:", str(self.client.user))
        print("ID:", str(self.client.user.id))
        print('----------')

        print("Running MOTW function. . .")
        congrats_messages = ["Congratulations to member of the week, %s! That's all you get.",
                            "How does it feel to be Member of the Week? Just ask %s!.",
                            "Being member of the week honestly means nothing and we're all going to die. Congratulations %s!",
                            "We don't usually like to play favorites but %s is definitely member of the week!",
                            "Congratulations to %s on being this week's Member of the Week! We appreciate ya!"]

        for server in self.client.guilds:

            #Checks to see if the member is an admin, bot/self, or regular member
            members = []
            admins = []
            for member in server.members:
                if member.bot:
                    pass #does not add bot/self to the member listener
                else:
                    for role in member.roles:
                        if member.guild_permissions.administrator:
                            admins.append(member.mention)
                    members.append(member.mention)

            #Removes admins from members list
            normal_members = (set(members)-set(admins))
            members = list(normal_members)


            for channel in server.channels:
                if "member" in channel.name and "week" in channel.name:

                    try:
                        #Checks to see when last MOTW message was sent
                        pins = await discord.abc.Messageable.pins(channel)
                        last_pin = pins[-1].created_at
                        when_message_sent = datetime.date(last_pin.year, last_pin.month, last_pin.day).isocalendar()[1]
                    except Exception as e:
                        when_message_sent = 53 #current_week will never be equal to this ; only 52 weeks in a year


                    #Grab current number Week
                    current_date = datetime.datetime.now()
                    current_week = datetime.date(current_date.year, current_date.month, current_date.day).isocalendar()[1]

                    if when_message_sent == current_week:
                        print("No new member of the week because one has already been picked for this week.")
                        pass
                    else:
                        random_member = random.choice(members)
                        message_choice = random.choice(congrats_messages) % str(random_member)
                        client_message = await channel.send(message_choice)
                        pin_client_message = await client_message.pin()
                        print("New member of the week selected.")

        print("Checking for birthdays. . .")
        time = datetime.datetime.now()
        #Getting list of admins for birthday message
        admins = []
        for server in client.guilds: #for every server
            for member in server.members: # go through all the members
                for role in member.roles: #check all of their roles
                    if role.name == settings['roles']['admin']: #if they're an admin
                        admins.append(str(member.name)) #then add them to the admin list

        #Checking to see whose birthday it is
        for server in client.guilds:
            for member in server.members:

                with open("birthdaydatabase.txt") as birthday_database:

                    dataset = json.loads("[" + birthday_database.read().replace("}\n{", "},\n{") + "]")

                    for i in range(len(dataset)): #go through each dataset
                        try:
                            for person in dataset[i][str(member)]:

                                birth_day = int(person['birth_day'])
                                birth_month = int(person['birth_month'])

                                todays_birthdays = []
                                if birth_day == time.day and birth_month == time.month:
                                    await member.send("Happy birthday from " + ', '.join(admins[:-1]) + " and " + admins[-1] + "!!") # actually sends birthday message
                                    todays_birthdays.append(member)

                                if len(todays_birthdays) == 0:
                                    print("No birthday messages sent today.")
                                else:
                                    print("Sent out birthday messages.")

                        except Exception as e:
                            #print(str(e))
                            continue


def setup(client):
    client.add_cog(OnReady(client))
