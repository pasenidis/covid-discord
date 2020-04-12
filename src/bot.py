import discord
from discord.ext import commands
import aiohttp

token = 'Null'  # DO NOT ENTER! CREATE A FILE WITH YOUR CREDENTIALS AND NEVER SHARE IT!

f = open('credentials.txt', 'r')
if f.mode == 'r':
    token = f.read()


class Bot(commands.Bot):
    async def on_ready(self):
        print('Starting up...')
        await self.change_presence(activity=discord.Game(name='covid, help'))


bot = Bot(command_prefix='covid, ')  # CHANGE THE PREFIX HERE

bot.load_extension('cogs.main')

bot.run(token)
