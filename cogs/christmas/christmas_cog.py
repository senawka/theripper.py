# a Christmas counter using Discord timestamps.
import discord
from discord.ext import commands
import datetime

class Christmas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def christmas(self, ctx):
        current_date = datetime.datetime.now()

        christmas_date = datetime.datetime(current_date.year, 12, 25)
        remaining_days = (christmas_date - current_date).days

        timestamp = f'<t:{int(christmas_date.timestamp())}:R>'
        message = f"Christmas is {timestamp}! 🎄"

        await ctx.send(message)

def setup(bot):
    bot.add_cog(Christmas(bot))