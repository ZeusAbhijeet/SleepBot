import discord
import Util
import random
from discord.ext import commands

class Announcements(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.AnnouncementChannelID = 835775311416786945
	
	async def AnnouncementEmbed(self, Podcaster, PodcastName, PodcastTopic, PodcastPoster = None):
		podcastEmbed = discord.Embed(title= "{} by {} is starting soon!".format(PodcastName, Podcaster),
								description= "Today's topic for the podcast is: \n**{}**. \n\nJoin the <#835775088539336764> Stage channel!\nㅤ".format(PodcastTopic),
								colour=random.randint(0, 0xffffff))
		podcastEmbed.add_field(name="Want to Get Notified for Podcasts?", value="Get the Podcast Ping roles for your favourite podcasts (or all of them cuz why not? <:Smirks:757906751063588912>) from <#835775268844339210> or [click here](https://discord.com/channels/740589508365385839/835775268844339210/835813552190783548)")
		if PodcastPoster != None:
			podcastEmbed.set_image(url=PodcastPoster)
		else:
			podcastEmbed.set_image(url="https://res.cloudinary.com/zeusabhijeet/image/upload/v1619981168/SleepBot/Announcements/Clinify-Originals-Poster.jpg")
		return podcastEmbed
	
	@commands.command(name = "announceYashvi")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceYashvi(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Yashvi", "Book Archives", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&829296249874022450>', embed = PodcastEmbed)

	@commands.command(name = "announceHritik")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceHritik(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Hritik Rahul and Solum Moss", "The Losers Talk", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&835804077404192779>', embed = PodcastEmbed)
	
	@commands.command(name = "announceAseem")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceAseem(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Aseem Srivastava", "Eatingbea", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&835804084963508234>', embed = PodcastEmbed)
	
	@commands.command(name = "announceSia")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceSia(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Sia Mulge", "Those Youth Terms", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&835804110786658305>', embed = PodcastEmbed)
	
	@commands.command(name = "announceVanshaj")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceVanshaj(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Vanshaj", "Internet Psychology 101", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&835804105275736134>', embed = PodcastEmbed)
	
	@commands.command(name = "announceSid")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceSid(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Sid Park", "Startups ki Saanp Seedhi", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&835804112863494186>', embed = PodcastEmbed)
	
	@commands.command(name = "announceViraj")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceViraj(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Viraj Raundal", "Observe: Tech and all the stuff around it!", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&829296550601031710>', embed = PodcastEmbed)
	
	@commands.command(name = "announceHarish")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceHarish(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Curious Harish", "Creator Club", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&829295982453194772>', embed = PodcastEmbed)
	
	@commands.command(name = "announceSakshi")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceSakshi(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Sakshi Soni", "The Quintessential Queens", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&838413457623744542>', embed = PodcastEmbed)
	
	@commands.command(name = "announceYogen")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceYogen(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Yogen", "Influenced Consumer", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&838413807435907083>', embed = PodcastEmbed)
	
	@commands.command(name = "announceGargi")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceGargi(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Gargi", "The Garspective Show : Understanding Within and Beyond", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&838414123514986556>', embed = PodcastEmbed)
	
	@commands.command(name = "announceStress")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceStress(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Deshna and Tanisha", "Successfully Stressed", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&838414286609973248>', embed = PodcastEmbed)

def setup(client):
	client.add_cog(Announcements(client))
