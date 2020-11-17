import discord
import random
import asyncio
import sqlite3
import Util
from discord.ext import commands

class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client
		conn = sqlite3.connect('Database.db')
		c = conn.cursor()
		c.execute("SELECT info FROM general_table WHERE title='STARBOARD-EMOJI';")
		self.starboard_emoji = c.fetchone()
		c.execute("SELECT channel_ID FROM channel_table WHERE title='STARBOARD';")
		self.starboard_chnl = c.fetchone()
		conn.close()
		self.starboard_emoji = int(self.starboard_emoji[0])
	
	async def fun_command_embed(self, ctx, title_string, description_string, image_url):
		embed = discord.Embed(title = title_string,
			description = description_string,
			colour = random.randint(0,0xffffff)
		)
		embed.set_image(url = image_url)
		embed.set_footer(text = "Requested by {}".format(ctx.message.author), icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = embed)
	
	
	
	@commands.command(name='ban')
	@commands.cooldown(1, 300, commands.BucketType.user)
	async def ban(self, ctx, target : discord.Member = None, *, reason = "none"):
		title = "{} is Flaming everyone, Dodge !!".format(ctx.author.name) if target == None else "{} is Flaming {} into the Oblivion with the Ban Flame!".format(ctx.author.name, target.name)
		description = "The Fuel Has been Injected! Time to Ban!" if reason == "none" else "The Fuel Has been Injected! Time to Ban!\n**Reason:** {}".format(reason)
		url = 'https://cdn.discordapp.com/attachments/755740543358861383/772007520532168715/banpower.gif'
		await self.fun_command_embed(ctx, title, description, url)
	@ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			embed = discord.Embed(title = "Failed To Run Command", description = "**Reason:** {}".format(error), colour = random.randint(0,0xffffff))
			await ctx.send(embed = embed)
	
	@commands.command(name='kick')
	@commands.cooldown(1, 300, commands.BucketType.user)
	async def kick(self, ctx, target : discord.Member = None, *, reason = "none"):
		title = "{} is Kicking Everyone Out of the Party!".format(ctx.author.name) if target == None else "{} is Kicking {} Out of the Party!".format(ctx.author.name, target.name)
		description = "Get Out or Get Rekt!" if reason == "none" else "Get Out or Get Rekt!\n**Reason:** {}".format(reason)
		url = 'https://cdn.discordapp.com/attachments/771081877414346772/771991494923386880/tenor_1.gif'
		await self.fun_command_embed(ctx, title, description, url)
	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			embed = discord.Embed(title = "Failed To Run Command", description = "**Reason:** {}".format(error), colour = random.randint(0,0xffffff))
			await ctx.send(embed = embed)
	
	@commands.command(name='shoot')
	@commands.cooldown(1, 300, commands.BucketType.user)
	async def shoot(self, ctx, target : discord.Member = None, *, reason = "none"):
		title = "{} just shot everyone!".format(ctx.author.name) if target == None else "{} is Shooting {} Out of the Party!".format(ctx.author.name, target.name)
		description = "The gun's loaded! I taught y'all how to dodge! Right?" if reason == "none" else "C'mon I taught you how to dodge!\n**Reason:** {}".format(reason)
		url = 'https://cdn.discordapp.com/attachments/755740543358861383/772012691081527296/shooting.gif'
		await self.fun_command_embed(ctx, title, description, url)
	@shoot.error
	async def shoot_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			embed = discord.Embed(title = "Failed To Run Command", description = "**Reason:** {}".format(error), colour = random.randint(0,0xffffff))
			await ctx.send(embed = embed)
			
	@commands.command(name='gib_rose')
	@commands.cooldown(1, 300, commands.BucketType.user)
	async def gib_rose(self, ctx, target : discord.Member = None, *, reason = "none"):
		title = "{} just gave a Rose!".format(ctx.author.name) if target == None else "{} is giving a rose to {}, Celebrate!".format(ctx.author.name, target.name)
		description = "Take this rose pls" if reason == "none" else "Take this rose pls\n**Reason:** {}".format(reason)
		url = 'https://cdn.discordapp.com/attachments/729619832097472552/776024679684505600/gibrose.gif'
		await self.fun_command_embed(ctx, title, description, url)
	@gib_rose.error
	async def gib_rose_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			embed = discord.Embed(title = "Failed To Run Command", description = "**Reason:** {}".format(error), colour = random.randint(0,0xffffff))
			await ctx.send(embed = embed)

	@commands.Cog.listener()
	async def on_reaction_add(self, ctx, user):
		try:
			mychn = self.client.get_channel(int(self.starboard_chnl[0]))
			if((ctx.emoji.id == self.starboard_emoji) and
				ctx.count == 3 and
				ctx.message.channel != mychn and
				(not(ctx.message.id in Util.HIGHLIGHT_HIST))):
				embed = discord.Embed(description = "{}\n\n".format(ctx.message.content),
						colour = random.randint(0, 0xffffff))
				embed.add_field(name = "Source", value = "[Link]({})".format(ctx.message.jump_url), inline = False)
				embed.set_author(name = ctx.message.author, icon_url = ctx.message.author.avatar_url)
				Util.HIGHLIGHT_HIST.append(ctx.message.id)
				await mychn.send(embed = embed)
		except Exception as error:
			return


	
def setup(client):
	client.add_cog(Fun(client))


