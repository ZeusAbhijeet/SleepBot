import discord
import sqlite3
import random
import Util
import asyncio
from discord.ext import commands

class Point(commands.Cog):
	"""
	Contains commands for checking user's Bluelearn Coins balance and leaderboard
	"""
	def __init__(self, client):
		self.client = client

	@commands.command(name = 'give_coins', aliases = ['give_points'])
	@commands.has_role('SleepBot Admin')
	async def give_coins(self, ctx, target: discord.Member = None, amount = 0):
		await Util.command_log(self.client, ctx, "give_points")
		if target == None:
			return
		if target.id in Util.POINT:
			Util.POINT[target.id] += amount
		else:
			Util.POINT[target.id] = amount
		await ctx.send(f'Gave {target} {amount} coins')
	
	@commands.command(name='coins', 
		aliases=['point', 'points', 'coin'], 
		help="Shows the Coins that the mentioned user has.")
	@Util.is_point_cmd_chnl()
	async def coins(self, ctx, target: discord.Member = None):
		await Util.command_log(self.client, ctx, "points")
		total_point = dict(Util.POINT)
		for user in Util.DB_POINT:
			if user[0] in total_point:
				total_point[user[0]] += user[1]
			else:
				total_point[user[0]] = user[1]
		if target == None :
			await ctx.send("Mention a user to check points.")
			return
		else:
			msg = await ctx.send(embed = Util.loading_embed)
			if not (target.id in total_point):
				total_point[target.id] = 0
			embed = discord.Embed(title = "User {}'s Coins".format(target.name),
				description = "{} has {} coins since reset.".format(target.name,total_point[target.id]),
				colour = random.randint(0,0xffffff)
				)
			await msg.edit(embed = embed)
			return
	@coins.error
	async def coins_error(self, ctx, error):
		if isinstance(error, commands.CheckFailure):
			await ctx.send("Points command can only be used in <#{}> channel!".format(Util.POINTCMD))
		else:
			await Util.ErrorHandler(ctx, error)
	
	@commands.command(name='top', 
		aliases=['leaderboard', 'all_coins', 'all_points', 'lb'], 
		help="Shows the top 20 users in leaderboard.")
	@Util.is_point_cmd_chnl()
	async def top(self, ctx):
		await Util.command_log(self.client, ctx, "top")
		msg = await ctx.send(embed = Util.loading_embed)
		total_point = dict(Util.POINT)
		for user in Util.DB_POINT:
			if user[0] in total_point:
				total_point[user[0]] += user[1]
			else:
				total_point[user[0]] = user[1]
		top_20 = 1
		total_point = sorted(total_point.items(), key = lambda kv: kv[1])
		total_point.reverse()
		embed = discord.Embed(title = "Coins Leaderboard",
			description = "Top Coins Since Last Reset.",
			colour = random.randint(0,0xffffff)
			)
		for user in total_point:
			username = self.client.get_user(int(user[0]))
			if username == None:
				continue
			embed.add_field(name = "{} : {}".format(top_20, username.display_name), value = user[1])
			top_20 += 1
			if top_20 == 21:
				break
		await msg.edit(embed = embed)
	@top.error
	async def top_error(self, ctx, error):
		if isinstance(error, commands.CheckFailure):
			await ctx.send("Points command can only be used in <#{}> channel!".format(Util.POINTCMD))
		else:
			await Util.ErrorHandler(ctx, error)
	
	@commands.Cog.listener()
	async def on_message(self, ctx):
		if not Util.is_point_chnl(ctx):
			return
		if ctx.author.bot:
			return
		member = await ctx.guild.fetch_member(ctx.author.id)
		if random.randint(0,200) == 0:
			emoji = '🎖'
			await ctx.add_reaction(emoji)
			if ctx.author.id in Util.POINT:
				Util.POINT[ctx.author.id] += 5
			else:
				Util.POINT[ctx.author.id] = 5

def setup(client):
	client.add_cog(Point(client))
