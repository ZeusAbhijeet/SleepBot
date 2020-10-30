import discord
import random
from discord.ext import commands

class Info(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name='ping', aliases=['latency'], help='Pong!')
	async def ping(self, ctx):
		embed=discord.Embed(title='Pong!', 
			description=f'Ping = {round(self.client.latency * 1000)}ms', 
			colour=random.randint(0,0xffffff)
		)
		embed.set_footer(text=f'Requested by {ctx.author}')
		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Info(client))
