# Importing Libraries required for the bot to function
import discord
import os
import sqlite3
import asyncio
# Import Util.py to get tasks
import Util
from discord.ext import commands, tasks
from pretty_help import PrettyHelp
from dotenv import load_dotenv
from itertools import cycle
from datetime import datetime
from discord_slash import SlashCommand

# Getting Token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Adding Intents
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

# Setting Prefix
client = commands.Bot(command_prefix = ['?'], case_insensitive=True, intents = intents, help_command=PrettyHelp(active=60))
slash = SlashCommand(client, sync_commands=True)

#Startup routine
@client.event
async def on_ready():
	print('Bot is ready.')
	print(f'Logged in as: {client.user.name} ID: {client.user.id}')
	print(f'Online in Guilds:')
	for server in client.guilds:
		print(f'Guild name: {server.name}')
		print(f'Guild ID: {server.id}')
	await client.change_presence(activity=discord.Game(name="Get vaccinated | ?help"))

if __name__ == '__main__':
	extensions = {'Info', 'Point', 'Fun', 'Mod', 'CodeHelp', 'Rule', 'Welcome', 'Study', 'Forest', 'Announcements'} 
	for extension in extensions:
		try:
			client.load_extension(extension)
			print(f'Loaded Cog {extension} successfully')
		except Exception as error:
			print(f'Failed to load Cog {extension}. Reason: {error}')
	# For taking backup of DB
	client.loop.create_task(Util.Backup(client))

# The following commands will be used to load Cogs
# They are locked behind a has_role check which requires the user to have the "SleepBot Admin" role
# This can be changed to allow people having Administrator permissions by changing the check to
# @commands.has_permissions(administrator=True)
@client.command(name='load')
@commands.has_role("SleepBot Admin")
async def load(ctx, extension):
	if extension == '':
		await ctx.send("Please enter a valid cog.")
	try:
		client.load_extension(extension)
		await ctx.send(f'Loaded {extension}!')
	except Exception as error:
		await ctx.send(f'Failed to load Cog {extension}. Reason: {error}')

@client.command(name='unload')
@commands.has_role("SleepBot Admin")
async def unload(ctx, extension):
	if extension == '':
		await ctx.send("Please enter a valid cog.")
	try:
		client.unload_extension(extension)
		await ctx.send(f'Unloaded {extension}!')
	except Exception as error:
		await ctx.send(f'Failed to unload Cog {extension}. Reason: {error}')

@client.command(name='reload')
@commands.has_role("SleepBot Admin")
async def reload(ctx, extension):
	if extension == '':
		await ctx.send("Please enter a valid cog.")
	try:
		client.unload_extension(extension)
		client.load_extension(extension)
		await ctx.send(f'Reloaded {extension}!')
	except Exception as error:
		await ctx.send(f'Failed to reload Cog {extension}. Reason: {error}')

# Command to shut the bot down
# Again requires user to have "SleepBot Admin" role which can also be changed
@client.command(name='logout')
@commands.has_role("SleepBot Admin")
async def logout(ctx):
	await ctx.send("<a:Loading:771266181943918602>Logging Out")
	await client.close()
@logout.error
async def logout_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		await ctx.send(f'You do not have permission to run this command!')

client.run(TOKEN)
