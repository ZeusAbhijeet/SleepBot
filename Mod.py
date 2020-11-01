import discord
import asyncio
import sqlite3
import random
from discord.ext import commands

class Mod(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name='clear', aliases=['purge', 'delete'], help='Clears the given amount of messages. Clears 3 messages by default.')
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount=3):
		if amount < 0 or amount > 100:
			await ctx.send("Enter a number between 0 and 100")
		else:
			deleted = await ctx.channel.purge(limit=amount+1)
			msg = f'**Deleted {len(deleted)-1}/{amount} messages**!'
			embed = discord.Embed(title = 'Delete Messages',
				description = msg,
				colour = random.randint(0,0xffffff))
			await ctx.send(embed = embed, delete_after = 5)
	@clear.error
	async def clear_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f'You require Manage Messages Permission to run this command.')


def setup(client):
	client.add_cog(Mod(client))
