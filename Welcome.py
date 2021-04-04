import discord
import random
from discord import client
from discord.ext.commands.cog import Cog
import Util
from datetime import datetime
from discord.ext import commands

class Welcome(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	async def welcomeEmbedReturner(self, target : discord.Member):
		welcomeEmbed = discord.Embed(title = "Welcome to the Clinify Squad Discord Server!",
							description = "Make sure that you have a **verified email connected to your account** so that you can interact in the server. \nHere are a few things that you can do:",
							colour = random.randint(0, 0xffffff),
							url = 'https://www.clinify.in/')
		welcomeEmbed.add_field(name="Read the Rules", 
					value="Read the rules from the <#752804052278050817> channel and react to the rule message with the 📝 emoji.",
					inline=False)
		welcomeEmbed.add_field(name="Check out the Server Tutorial Video", 
					value="If you are new to discord, you can watch a tutorial video which will help you to go about the server.\n**PC tutorial:** [Click here](https://youtu.be/S17_XjFxSsQ)\n**Mobile tutorial:** Coming soon",
					inline=False)
		welcomeEmbed.add_field(name="Get Some Roles",
					value="Get some roles from <#752466815128436826> to change your name colour in server, get notified about announcements, join a club, or get some people to join you while studying.")
		welcomeEmbed.set_image(url='https://res.cloudinary.com/zeusabhijeet/image/upload/v1614530857/Clinify%20Stuff/Welcome_Banner.gif')
		welcomeEmbed.set_author(name=target.name, icon_url=target.avatar_url)
		return welcomeEmbed

	@commands.command(name='welcomedm')
	@commands.has_permissions(administrator = True)
	async def welcomedm(self, ctx, targetMember : discord.Member = None):
		if targetMember == None:
			targetMember = ctx.message.author
		await targetMember.send(embed = await self.welcomeEmbedReturner(targetMember))
		await ctx.send(f'Successfully sent DM to {targetMember}')
	
	@Cog.listener()
	async def on_member_join(self, member):
		await member.send(embed = await self.welcomeEmbedReturner(member))
		JoinLogEmbed = discord.Embed(title = "SleepBot Welcome DM Log",
								description = "Sent DM Message Successfully to: Username: {} ID: {} at {}".format(member, member.id, datetime.now()),
								colour = random.randint(0, 0xffffff))
		await self.client.get_channel(Util.LOG[0]).send(embed = JoinLogEmbed)

def setup(client):
	client.add_cog(Welcome(client))
