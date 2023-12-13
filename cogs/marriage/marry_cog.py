# WORK IN PROGRESS // FUNCTIONALITY IS THERE BUT NOT WORKING AS INTENDED

import discord
from discord.ext import commands
import json
import asyncio
import random

MarrySelf = [
    "You can't marry yourself!",
    "You married yourself.... oh wait, you can't.",
    "Just stick to using your hand.",
    "You can't.",
]

MarryBot = [
    "You can't marry a Discord bot!",
    "This is a Discord bot, not a real person.",
    "The Discord bot you are trying to marry is incapable of feeling love.",
    "Unable to marry... the bot? Seriously?"
]

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

    async def send_embed_message(self, ctx, content):
        embed = discord.Embed(description=content, color=discord.Color.from_rgb(255, 209, 220))
        await ctx.send(embed=embed)

    @commands.command()
    async def marry(self, ctx, user: discord.Member):
        if user == ctx.author:
            await self.send_embed_message(ctx, f"{ctx.author.mention} {random.choice(MarrySelf)}")
            return
        elif user.bot:
            await self.send_embed_message(ctx, f"{ctx.author.mention} {random.choice(MarryBot)}")
            return
        elif user == self.bot.user:
            await self.send_embed_message(ctx, "You can't marry the bot that is running this code!")
            return

        for marriage in self.marriageDb["marriages"]:
            if marriage["husband"] == str(ctx.author.id) and marriage["wife"] == str(user.id):
                await self.send_embed_message(ctx, "You are already married to this user!")
                return
            elif marriage["husband"] == str(user.id) and marriage["wife"] == str(ctx.author.id):
                await self.send_embed_message(ctx, "This user is already married to someone else!")
                return

        for marriage in self.marriageDb["marriages"]:
            if marriage["husband"] == str(ctx.author.id) or marriage["wife"] == str(ctx.author.id):
                await self.send_embed_message(ctx, "You can't have a harem!")
                return

        MentionedUser = user

        def check(reaction, user):
            return user == MentionedUser and str(reaction.emoji) == '✅' and reaction.message.id == proposalMessage.id

        embed = discord.Embed(title="Marriage Proposal", description=f"{user.mention}, {ctx.author.mention} is proposing to marry you. Do you accept? React with ✅ to accept.", color=discord.Color.from_rgb(255, 209, 220))
        proposalMessage = await ctx.send(embed=embed)
        await proposalMessage.add_reaction('✅')

        try:
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await self.send_embed_message(ctx, "Marriage proposal timed out.")
            return

        newMarriage = {
            "husband": str(ctx.author.id),
            "wife": str(user.id)
        }

        self.marriageDb["marriages"].append(newMarriage)
        self.saveMarriageDb()

        embed = discord.Embed(title="Congratulations!", description=f"{ctx.author.display_name} and {user.display_name} are now married!", color=discord.Color.from_rgb(255, 209, 220))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Marriage(bot))
