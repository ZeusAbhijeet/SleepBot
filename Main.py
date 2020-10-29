import discord
import os
import random
import asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '.s')

@client.event
async def on_ready():
	print('Bot is ready.')
	print(f'Logged in as: {client.user.name} ID: {client.user.id}')
	print(f'Online in Guilds:')
	for server in client.guilds:
		print(f'Guild name: {server.name}')
		print(f'Guild ID: {server.id}')

@client.command(name='ping', aliases=['latency'])
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


client.run(TOKEN)
