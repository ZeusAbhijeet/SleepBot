import discord
from discord.ext import commands

class Info(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name='ping', aliases=['latency'], help='Pong!')
	async def ping(self, ctx):
		embed=discord.Embed(title='Pong!', 
			description=f'Ping = {round(self.client.latency * 1000)}ms', 
			colour=discord.Colour.blue())
		embed.set_footer(text=f'Requested by {ctx.author}')
		await ctx.send(embed=embed)
		#await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


def setup(client):
	client.add_cog(Info(client))
