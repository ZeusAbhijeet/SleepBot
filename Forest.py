import discord
import random
import requests
import json
import Util
from discord.ext import commands
from dpymenus import Page, PaginatedMenu

class Forest(commands.Cog):
	"""
	Contains commands regarding Clinify Forest
	"""
	def __init__(self, client):
		self.client = client
	
	@commands.command(name = 'forest_leaderboard', aliases = ['flb', 'forest_lb', 'cflb', 'bflb'], help = "Fetches top 10 users from Clinify Forest Leaderboard.")
	async def forest_leaderboard(self, ctx):
		msg = await ctx.send(embed = Util.loading_embed)
		LbEmbed = discord.Embed(title = "Blue Forest Leaderboard",
							description = """Following are the top 15 users on Blue Forest Leaderboard.
							For more users, go to the **[Blue Forest Leaderboard Website](https://clinifyforest.herokuapp.com/leaderboard)**""",
							colour = random.randint(0, 0xffffff))
		response = requests.get("https://clinifyforest.herokuapp.com/clinifyforest/api/getlb/15")
		Rank = 1
		for i in response.json():
			LbEmbed.add_field(name = "{}. {}".format(Rank, i["discord_tag"]),
						value="Trees Planted : **{}** \nCoins : **{}**".format(i["trees"], i["coins"]), inline = True)
			Rank = Rank + 1
		LbEmbed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await msg.edit(embed = LbEmbed)
	@forest_leaderboard.error
	async def cflbError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = 'forest_user', aliases = ['fuser', 'fprofile', 'cfuser', 'bfuser'], help = "Fetches stats about the user from Clinify Forest.")
	async def forest_user(self, ctx, TargetUser : discord.Member = None):
		msg = await ctx.send(embed = Util.loading_embed)
		if TargetUser == None:
			TargetUser = ctx.author
		response = requests.get("https://clinifyforest.herokuapp.com/clinifyforest/api/getuser/{}".format(TargetUser.id))
		UserInfo = response.json()
		UserEmbed = discord.Embed(title = "Blue Forest User Info",
								description = "The following is the Blue Forest stats about <@!{}>:".format(UserInfo["id"]),
								colour = random.randint(0, 0xffffff))
		if UserInfo["avatar"] == None:
			UserEmbed.set_thumbnail(url="https://res.cloudinary.com/zeusabhijeet/image/upload/v1619698559/SleepBot/Clinify%20Forest/Default.png")
		else:
			UserEmbed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{}/{}.png".format(UserInfo["id"], UserInfo["avatar"]))
		UserEmbed.add_field(name="Discord ID:", value="{}".format(UserInfo["discord_tag"]), inline = True)
		UserEmbed.add_field(name="Trees Planted:", value="{}".format(UserInfo["trees"]), inline= True)
		UserEmbed.add_field(name="Dead Trees:", value="{}".format(UserInfo["deadtrees"]), inline=True)
		UserEmbed.add_field(name="Coins:", value="{}".format(UserInfo["coins"]), inline=True)
		UserEmbed.add_field(name="Level:", value="{}".format(UserInfo["level"]), inline=True)
		UserEmbed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await msg.edit(embed = UserEmbed)
	@forest_user.error
	async def cfuserError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)

def setup(client):
	client.add_cog(Forest(client))
