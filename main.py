#!/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio
import os
import datetime

async def start_bot():
    bot = commands.Bot(command_prefix='pip ', intents=discord.Intents.all(), help_command=None)

    cog_counts = {}
    
    for folder_name in os.listdir('cogs'):
        folder_path = os.path.join('cogs', folder_name)
        
        if not os.path.isdir(folder_path):
            continue
        
        cog_count = 0
        
        for file_name in os.listdir(folder_path):
            if file_name.endswith('_cog.py'):
                cog_count += 1
                cog_name = file_name[:-3]
                cog_path = f'cogs.{folder_name}.{cog_name}'
                bot.load_extension(cog_path)
        
        if cog_count > 0:
            cog_counts[folder_name] = cog_count

    @bot.event
    async def on_ready():
        server_count = len(bot.guilds)
        bot.start_time = datetime.datetime.now()
        activity = discord.Activity(type=discord.ActivityType.listening, name=f'to {server_count} server(s)')
        await bot.change_presence(activity=activity)
        
        cog_info = ", ".join([f"{folder}: {count} cog(s)" for folder, count in cog_counts.items()])
        
        print(f'Bot is running. Connected to {server_count} server(s). Loaded {len(bot.cogs)} cog(s) in {len(cog_counts)} folder(s): {cog_info}.')

    return bot

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    bot = loop.run_until_complete(start_bot())

    with open('token.txt') as t:
        token = t.read()
    bot.run(token)