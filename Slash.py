"""
This is a test cog that I added to test Slash Commands. Please ignore.
"""

import discord
import random
import Util
from discord_slash import cog_ext, SlashCommand
from discord.ext import commands

class Slash_Commands(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	guild_ids = Util.guild_ids

	@cog_ext.cog_slash(name='ping', description="Pong! Shows the latency of the bot", guild_ids=guild_ids)
	async def _ping(self, ctx):
		ping_embed=discord.Embed(title='Pong!', 
			description=f'Ping = {round(self.client.latency * 1000)}ms', 
			colour=random.randint(0,0xffffff)
		)
		ping_embed.set_footer(text=f'Requested by {ctx.author}')
		await ctx.defer()
		await ctx.send(embed=ping_embed)

def setup(client):
	client.add_cog(Slash_Commands(client))
