# WORK IN PROGRESS // FUNCTIONALITY IS THERE BUT NOT WORKING AS INTENDED

import discord
from discord.ext import commands
import json
import asyncio

class Marriage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.marriageDb = self.loadMarriageDb()

    def loadMarriageDb(self):
        with open("marriages.json", "r") as file:
            return json.load(file)

    def saveMarriageDb(self):
        with open("marriages.json", "w") as file:
            json.dump(self.marriageDb, file, indent=4)

    @commands.command()
    async def marry(self, ctx, user: discord.Member):
        if user == ctx.author or user == self.bot.user:
            await ctx.send("You can't marry yourself or a bot!")
            return

        for marriage in self.marriageDb["marriages"]:
            if marriage["husband"] == str(ctx.author.id) and marriage["wife"] == str(user.id):
                await ctx.send("You are already married to this user!")
                return
            elif marriage["husband"] == str(user.id) and marriage["wife"] == str(ctx.author.id):
                await ctx.send("This user is already married to someone else!")
                return

        for marriage in self.marriageDb["marriages"]:
            if marriage["husband"] == str(ctx.author.id) or marriage["wife"] == str(ctx.author.id):
                await ctx.send("You can't have a harem!")
                return

        def check(reaction, user):
            return user == user and str(reaction.emoji) == '✅' and reaction.message.id == proposalMessage.id

        proposalMessage = await ctx.send(f"{user.mention}, {ctx.author.mention} is proposing to marry you. Do you accept? React with ✅ to accept.")
        await proposalMessage.add_reaction('✅')

        try:
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f"Marriage proposal timed out.")
            return

        newMarriage = {
            "husband": str(ctx.author.id),
            "wife": str(user.id)
        }

        self.marriageDb["marriages"].append(newMarriage)
        self.saveMarriageDb()

        await ctx.send(f"{ctx.author.display_name} and {user.display_name} are now married!")

def setup(bot):
    bot.add_cog(Marriage(bot))