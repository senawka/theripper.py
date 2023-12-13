# status of the server the bot is running on.

import discord
from discord.ext import commands
import platform
import datetime

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.startTime = datetime.datetime.utcnow()

    @commands.command()
    async def status(self, ctx):
        uptime = datetime.datetime.utcnow() - self.bot.startTime
        uptimestr = self.getRelativeTime(uptime)

        osInfo = f"{platform.system()} {platform.release()}"
        latency = round(self.bot.latency * 1000)

        embed = discord.Embed(title="Server Status", color=discord.Color.from_rgb(255, 209, 220))
        embed.add_field(name="Uptime", value=uptimestr, inline=False)
        embed.add_field(name="OS", value=osInfo, inline=False)
        embed.add_field(name="Latency", value=f"{latency} ms", inline=False)

        await ctx.send(embed=embed)

    @staticmethod
    def getRelativeTime(delta):
        seconds = delta.total_seconds()
        intervals = (
            ('weeks', 604800),
            ('days', 86400),
            ('hours', 3600),
            ('minutes', 60),
            ('seconds', 1),
        )
        for name, count in intervals:
            value = int(seconds // count)
            if value:
                return f"{value} {name} ago"

        return "just now"

def setup(bot):
    bot.add_cog(Status(bot))
