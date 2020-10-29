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

if __name__ == '__main__':
	extensions = {'Info'} #'Points, 'Mod', 'Util'
	for extension in extensions:
		try:
			client.load_extension(extension)
			print(f'Loaded Cog {extension} successfully')
		except Exception as error:
			print(f'Failed to load Cog {extension}. Reason: {error}')


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

@client.command(name='logout')
@commands.has_role("SleepBot Admin")
async def logout(ctx):
	await ctx.send("Logging Out")
	await client.logout()
@logout.error
async def logout_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		await ctx.send(f'You do not have permission to run this command!')


client.run(TOKEN)
