import discord
import random
from discord.ext import commands

class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	async def fun_command_embed(self, ctx, title_string, description_string, image_url):
		embed = discord.Embed(title = title_string,
			description = description_string,
			colour = random.randint(0,0xffffff)
		)
		embed.set_image(url = image_url)
		embed.set_footer(text = "Requested by {}".format(ctx.message.author), icon_url = ctx.message.author.avatar_url)
		await ctx.send(embed = embed)
	
	@commands.command(name='avatar', aliases=['av','profile', 'pfp'], help='Sends the Avatar of the Mentioned User. If no one is mentioned then sends the Avatar of the Author.')
	async def avatar(self, ctx, *, target: discord.Member = None):
		embed=discord.Embed(title='Avatar', colour=random.randint(0,0xffffff))
		if target == None:
			pfp_url = ctx.message.author.avatar_url
			embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
		else:
			pfp_url = target.avatar_url
			embed.set_author(name=target, icon_url=target.avatar_url)
		embed.set_image(url=pfp_url)
		embed.set_footer(text="Requested by {}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	
	@commands.command(name='ban', help="Ban the mentioned user I guess.")
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
	
	@commands.command(name='kick', help="Kick the mentioned user I guess.")
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
	
	@commands.command(name='shoot', help="Shoot the mentioned user I guess.")
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
			
	@commands.command(name='gib_rose', help="Give a rose to the mentioned user I guess.")
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

	
def setup(client):
	client.add_cog(Fun(client))


