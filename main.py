import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])

settings['token'] = ''.join(settings['token'].split('/secret/'))

intents = discord.Intents.default()  # Allow the use of custom intents
intents.members = True

ADMINS = [528619852106170368, 504324277789523972]


class GalaxyBot(discord.Client):
    async def on_ready(self):

        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith(f"{settings['prefix']} rewrite") and message.author.id in ADMINS:
            await message.channel.send(message.content.split(f"{settings['prefix']} rewrite")[1])
            await message.delete()
        elif message.content.startswith(f"{settings['prefix']} hello"):
            print(message)
            await message.channel.send('Hello World!')

            guild = message.guild
            members = []
            for member in guild.members:
                members.append(member)
            await message.channel.send(members)

            for i in message.guild.channels:
                if i.id == 925688053404696596:
                    await i.edit(name=f"Members: {message.guild.member_count}")
                    print(i)


client = GalaxyBot()
client.run(settings['token'])
