import discord
import sqlite3
import random
import Util
import asyncio
from discord.ext import commands

class Point(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name = 'give_points')
	@commands.has_role('SleepBot Admin')
	async def give_points(self, ctx, target: discord.Member = None, amount = 0):
		if target == None:
			return
		if target.id in Util.POINT:
			Util.POINT[target.id] += amount
		else:
			Util.POINT[target.id] = amount
		await ctx.send(f'Gave {target} {amount} points')
	
	@commands.command(name='points', aliases=['point', 'all_points'])
	async def points(self, ctx, target: discord.Member = None):
		total_point = dict(Util.POINT)
		for user in Util.DB_POINT:
			if user[0] in total_point:
				total_point[user[0]] += user[1]
			else:
				total_point[user[0]] = user[1]
		if target != None:
			if not (target.id in total_point):
				total_point[target.id] = 0
			embed = discord.Embed(title = f"User {target.name}'s points",
				description="{} has {} points".format(target.name, total_point[target.id]),
				colour=random.randint(0,0xffffff)
				)
			await ctx.send(embed=embed)
			return
	
		top_20 = 1
		total_point = sorted(total_point.items(), key = lambda kv: kv[1])
		total_point.reverse()
		embed = discord.Embed(title = 'Point Leaderboard',
			description = "Top Points Since Last Reset.",
			colour = random.randint(0,0xffffff)
			)
		for user in total_point:
			embed.add_field(name = "{} : {}".format(top_20, ctx.guild.get_member(user[0])), value = user[1])
			top_20 += 1
			if top_20 == 1:
				break
		await ctx.send(embed=embed)



def setup(client):
	client.add_cog(client)
