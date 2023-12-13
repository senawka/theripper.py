# sends the bot's oauth link to invite it to other servers.
# currently has administrative permissions; will change in the future.

import discord
from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="The Ripper OAuth2", color=0xFFC0CB, description="[Invite Link](https://discord.com/api/oauth2/authorize?client_id=1035012653376098366&permissions=8&scope=bot)")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Invite(bot))
