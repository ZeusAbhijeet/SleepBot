import discord
import asyncio
import sqlite3
import random
import Util
from discord.ext import commands
from dpytools.parsers import to_timedelta, to_lower
from dpytools.checks import any_of_permissions
from datetime import datetime

class Mod(commands.Cog):
	"""
	Contains Moderation commands for clearing messages and adding slowmode to a channel
	"""
	def __init__(self, client):
		self.client = client

	@commands.command(name='clear', 
		aliases=['purge', 'delete'], 
		help='Clears the given amount of messages. Clears 3 messages by default.')
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount=3):
		await Util.command_log(self.client, ctx, "clear")
		await ctx.message.delete()
		if amount < 0 or amount > 100:
			await ctx.send("Enter a number between 0 and 100")
		else:
			deleted = await ctx.channel.purge(limit=amount)
			msg = f'Deleted **{len(deleted)}/{amount}** messages!'
			embed = discord.Embed(title = 'Delete Messages',
				description = msg,
				colour = random.randint(0,0xffffff))
			await ctx.send(embed = embed, delete_after = 5)
	@clear.error
	async def clear_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f'You require Manage Messages Permission to run this command.')
		else:
			await Util.ErrorHandler(ctx, error)

	@commands.command(name='clearemote',
		aliases=['purgeemote', 'deleteemote', 'clearemotes', 'purgeemotes', 'deleteemotes'],
		help='Clears emotes')
	@commands.has_permissions(manage_messages=True)
	async def clearemote(self, ctx, amount=3):
		await Util.command_log(self.client, ctx, "clearemote")
		await ctx.message.delete()
		deleted = 0
		saveamount = amount
		msgList = []
		if amount > 100 or amount < 1:
			return await ctx.send("Enter a number between 0 and 100")
		embed_msg = await ctx.send(embed = discord.Embed(description="<a:bot_loading:809318632723185714> Clearing out **{}** emotes...".format(amount)))
		async for msg in ctx.channel.history(limit=1000):
			if amount <= 0:
				break
			if msg.content.startswith("<") or msg.content.endswith(">"):
				amount -= 1
				deleted += 1
				msgList.append(msg)
		await ctx.channel.delete_messages(msgList)
		embed = discord.Embed(title = 'Delete Emotes',
				description = "Deleted **{}/{}** emotes!".format(deleted, saveamount),
				colour = random.randint(0,0xffffff))
		await embed_msg.edit(embed = embed, delete_after = 5)
	@clearemote.error
	async def clearemote_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f'You require Manage Messages Permission to run this command.')
		else:
			await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = 'clearuser',
		aliases = ['purgeuser', 'cleanuser', 'clearusers', 'purgeusers', 'cleanusers'],
		help = "Clears messages from mentioned user")
	@commands.has_permissions(manage_messages=True)
	async def clearuser(self, ctx, target: discord.Member = None, amount = 3):
		await Util.command_log(self.client, ctx, "clearuser")
		await ctx.message.delete()
		saveamount = amount
		deleted = 0
		msgList = []
		if amount > 100 or amount < 0:
			return await ctx.send("Enter a number between 0 and 100")
		embed_msg = await ctx.send(embed = discord.Embed(description="<a:bot_loading:809318632723185714> Deleting **{}** messages sent by <@!{}>...".format(amount, target.id)))
		async for msg in ctx.channel.history(limit = 1000):
			if amount <= 0:
				break
			if msg.author.id == target.id:
				amount -= 1
				deleted += 1
				msgList.append(msg)
		await ctx.channel.delete_messages(msgList)
		embed = discord.Embed(title = 'Delete Messages', 
			description = "Deleted **{}/{}** messages".format(deleted,saveamount),
			colour = random.randint(0, 0xffffff))
		await embed_msg.edit(embed = embed, delete_after = 5)
	@clearuser.error
	async def clearuser_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f'You require Manage Messages Permission to run this command.')
		else:
			await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = 'clearonly',
		aliases = ['purgeonly','cleanonly'],
		help = "Clears messages containing a specific word")
	@commands.has_permissions(manage_messages=True)
	async def clearonly(self, ctx, txt = '', amount = 5):
		await Util.command_log(self.client,ctx,"clearonly")
		await ctx.message.delete()
		deleted = 0
		saveamount = amount
		onlyStart = False
		msgList = []
		if amount > 100 or amount < 0:
			return await ctx.send("Enter a number between 0 and 100")
		if txt[0] == '^':
			onlyStart = True
		embed_msg = await ctx.send(embed = discord.Embed(description="<a:bot_loading:809318632723185714> Deleting **{}** messages containing '**{}**'...".format(amount, txt)))
		async for msg in ctx.channel.history(limit = 1000):
			if amount <= 0:
				break
			if onlyStart and msg.content.lower().startswith(txt[1:].lower()):
				amount -= 1
				await msg.delete()
				deleted += 1
			elif txt.lower() in msg.content.lower():
				amount -= 1
				deleted += 1
				msgList.append(msg)
		await ctx.channel.delete_messages(msgList)
		embed = discord.Embed(title = 'Delete Messages', 
			description = "Deleted **{}/{}** messages".format(deleted,saveamount),
			colour = random.randint(0, 0xffffff))
		await embed_msg.edit(embed = embed, delete_after = 5)
	@clearonly.error
	async def clearonly_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(f'You require Manage Messages Permission to run this command.')
		else:
			await Util.ErrorHandler(ctx, error)
	
	@commands.command(name='slowmode',
					aliases=['sm'],
					help="Adds slowmode to channel")
	@any_of_permissions(administrator=True, manage_messages=True)
	async def slowmode(self, ctx, SlowmodeDuration : to_timedelta, channel : discord.TextChannel = None):
		await Util.command_log(self.client, ctx, "slowmode")
		if channel is None:
			channel = ctx.channel
		else: pass
		
		def check_message(message):
			return ((message.author == ctx.author) and (message.channel == ctx.channel))
		
		SlowmodeDurationInSeconds = SlowmodeDuration.total_seconds()
		if SlowmodeDurationInSeconds >= 30.0:
			msg = await ctx.send(embed = discord.Embed(title = "Are you sure?",
											description = "Are you sure you want to set slowmode of {}s? (yes/no)".format(SlowmodeDurationInSeconds),
											colour = discord.Colour.red()))
			Confirmation = await self.client.wait_for('message', timeout=60.0, check = check_message)
			if to_lower(Confirmation.content) == 'no':
				await ctx.send(embed = discord.Embed(title="Command Cancelled",
											description = "The command was cancelled",
											colour = discord.Colour.red()),
								delete_after = 5)
				await msg.delete()
				return
		
		if SlowmodeDurationInSeconds >= 21600.0:
			await ctx.send("Cannot set slowmode for more than 6 hours")
			return

		await channel.edit(slowmode_delay = int(SlowmodeDurationInSeconds))
		await ctx.send(embed = discord.Embed(title = "Slowmode",
											description = "Successfully set slowmode to **{}** in {}".format(SlowmodeDuration, channel.mention),
											colour = discord.Colour.green()))
	@slowmode.error
	async def slowmode_error(self, ctx, error):
		await Util.ErrorHandler(ctx, error)

def setup(client):
	client.add_cog(Mod(client))
