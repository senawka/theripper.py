import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        
        embed = discord.Embed()
        embed.title = "Pong!"
        
        if latency <= 100:
            embed.description = f"Latency: {latency}ms"
            embed.colour = discord.Color.green()
        else:
            embed.description = f"Latency: {latency}ms"
            embed.colour = discord.Color.red()
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))