# sends responses to messages if certain conditions are met.

import re
import random
import discord
from discord.ext import commands

DRG = [
    "Rock and stone.. Yeeaaahhh!",
    "Rock and stone forever!",
    "ROCK... AND... STONE!",
    "Rock and stone!",
    "For rock and stone!",
    "We are unbreakable!",
    "Rock and roll!",
    "Rock and roll and stone!",
    "That's it lads! Rock and stone!",
    "Like that! Rock and stone!",
    "Yeaahhh! Rock and stone!",
    "Rock solid!",
    "Come on guys! Rock and stone!",
    "If you don't rock and stone, you ain't comin' home!",
    "We fight for rock and stone!",
    "Rock and stone everyone!",
    "Rock and stone in the heart!",
    "Did I hear a rock and stone?",
    "Stone and rock!",
    "Stone and rock! Oh wait...",
    "Yeah yeah, rock and stone.",
]

class Response(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        content = message.content.lower()
        words = re.findall(r'\b\w+\b', content)
        ErWords = [word for word in words if word.endswith('er') and word != 'er']
        if ErWords and random.randint(1, 10) == 1:
            word = random.choice(ErWords)
            response = f"{word}? I hardly know her!"
            await message.channel.send(response)
        
        if "rock" in content or "stone" in content:
            voice_line = random.choice(DRG)
            await message.channel.send(voice_line)

def setup(bot):
    bot.add_cog(Response(bot))