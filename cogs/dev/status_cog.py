# status of the server the bot is running on.

import discord
from discord.ext import commands
import os
import platform
import psutil
import datetime

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx):
        # Calculate uptime
        uptime = datetime.datetime.now() - self.bot.start_time
        uptime_str = self.get_relative_time(uptime)

        # Get server details
        os_name = platform.system()
        os_version = platform.release()

        # Get server latency
        latency = round(self.bot.latency * 1000)  # in milliseconds

        # Create embed
        embed = discord.Embed(title="Server Status", color=discord.Color.from_rgb(255, 209, 220))
        embed.add_field(name="Uptime", value=uptime_str, inline=False)
        embed.add_field(name="OS", value=f"{os_name} {os_version}", inline=False)
        embed.add_field(name="Latency", value=f"{latency} ms", inline=False)

        await ctx.send(embed=embed)

    def get_relative_time(self, delta):
        seconds = delta.total_seconds()
        intervals = (
            ('weeks', 604800),  # 60 * 60 * 24 * 7
            ('days', 86400),    # 60 * 60 * 24
            ('hours', 3600),    # 60 * 60
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