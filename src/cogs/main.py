import discord
from discord.ext import commands
import aiohttp


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def country(self, ctx, arg):
        print(f'Fetching country: {arg}')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://corona.lmao.ninja/countries/{arg}') as r:
                request = await r.json()
                embed = discord.Embed(
                    title="COVID-19.Tracker", description=f"**{request.get('country')}** / **{request.get('countryInfo').get('iso2')}**", color=0x00ff00)
                embed.add_field(
                    name="Cases", value=request.get('cases'), inline=True)
                embed.add_field(
                    name="Today Cases", value=request.get('todayCases'), inline=True)
                embed.add_field(
                    name="Recovered", value=request.get('recovered'), inline=True)
                embed.add_field(
                    name="Critical", value=request.get('critical'), inline=True)
                embed.add_field(
                    name="Deaths", value=request.get('deaths'), inline=True)
                embed.add_field(
                    name="Today Deaths", value=request.get('todayDeaths'), inline=True)
                embed.set_footer(text="https://covidtrack.tk")
                embed.set_thumbnail(url=request.get('countryInfo').get('flag'))
                # embed.set_thumbnail(
                # url=f"https://www.countryflags.io/{request.get('countryInfo').get('iso2')}/shiny/64.png")
                await ctx.channel.send(embed=embed)

    @commands.command(aliases=['worldwide', 'all'])
    async def world(self, ctx):
        print(f'Fetching worldwide stats')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://corona.lmao.ninja/countries/World') as r:
                request = await r.json()
                embed = discord.Embed(
                    title="COVID-19.Tracker", description="**Worldwide**", color=0x00ff00)
                embed.add_field(
                    name="Cases", value=request.get('cases'), inline=True)
                embed.add_field(
                    name="Today Cases", value=request.get('todayCases'), inline=True)
                embed.add_field(
                    name="Recovered", value=request.get('recovered'), inline=True)
                embed.add_field(
                    name="Critical", value=request.get('critical'), inline=True)
                embed.add_field(
                    name="Deaths", value=request.get('deaths'), inline=True)
                embed.add_field(
                    name="Today Deaths", value=request.get('todayDeaths'), inline=True)
                embed.set_footer(text="https://covidtrack.tk")
                embed.set_thumbnail(
                    url="https://d1nhio0ox7pgb.cloudfront.net/_img/g_collection_png/standard/512x512/earth.png")
                await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Main(bot))


def teardown(bot):
    bot.remove_cog('Main')
