from discord.ext import commands
import aiohttp


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def country(self, ctx, arg):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://corona.lmao.ninja/countries/{arg}') as r:
                request = await r.json()
                await ctx.send(f'data: {request}')


def setup(bot):
    bot.add_cog(Main(bot))


def teardown(bot):
    bot.remove_cog('Main')
