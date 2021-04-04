import discord
import random
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import Command
import Util
from datetime import datetime
from discord.ext import commands

class Study(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.FocusChannelID = 818131313810079744
		self.guildID = 740589508365385839
	
	async def StudyVCJoinMessage(self, member, NoOfRoles):
		StudyVCEmbed = discord.Embed(title = "It's Focus Time, {}!".format(member.name),
								description = "To help you focus, you have been muted in all channels except <#770940461337804810> and the music channels.",
								colour = random.randint(0, 0xffffff))
		StudyVCEmbed.add_field(name="How do I get unmuted?", value="You will be unmuted automatically when you leave the Study VCs.", inline = False)
		if random.randint(0, 200-NoOfRoles) == 0:
			StudyVCEmbed.set_image(url='https://res.cloudinary.com/zeusabhijeet/image/upload/v1615206699/SleepBot/Study%20Commands/Study_you_b_words.png')
		else:
			StudyVCEmbed.set_image(url='https://res.cloudinary.com/zeusabhijeet/image/upload/v1615211844/SleepBot/Study%20Commands/focus_you_b_words.gif')
		return StudyVCEmbed
	
	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		if before.channel is None and after.channel is not None:
			guild = self.client.get_guild(self.guildID)
			NoOfRoles = len(guild.get_member(member.id).roles)
			if after.channel.id == 770670934565715998 and not member.bot:
				await self.client.get_channel(self.FocusChannelID).send("<@!{}>".format(member.id))
				await self.client.get_channel(self.FocusChannelID).send(embed = await self.StudyVCJoinMessage(member, NoOfRoles))
			elif after.channel.id == 818011398231687178 and not member.bot:
				await self.client.get_channel(self.FocusChannelID).send("<@!{}>".format(member.id))
				await self.client.get_channel(self.FocusChannelID).send(embed = await self.StudyVCJoinMessage(member, NoOfRoles))
		else:
			return

def setup(client):
	client.add_cog(Study(client))
