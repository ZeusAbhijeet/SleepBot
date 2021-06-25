import discord
from discord.ext.commands import errors
import Util
import random
from discord.ext import commands

class Announcements(commands.Cog):
	"""
	Contains commands for making annoucements for BlueLearn Originals
	"""
	def __init__(self, client):
		self.client = client
		self.AnnouncementChannelID = 835775311416786945
	
	async def AnnouncementEmbed(self, Podcaster, PodcastName, PodcastTopic, PodcastPoster = None):
		podcastEmbed = discord.Embed(title= "{} : {} by {} is starting soon!".format(PodcastName, PodcastTopic, Podcaster),
								description= "Join the <#835775088539336764> Stage channel!\nㅤ".format(PodcastTopic),
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
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&829296249874022450> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceYashvi.error
	async def YashviError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)

	@commands.command(name = "announceHritik")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceHritik(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Hritik Rahul and Solum Moss", "The Losers Talk", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&835804077404192779> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceHritik.error
	async def HritikError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = "announceAseem")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceAseem(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Aseem Srivastava", "Eatingbea", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&835804084963508234> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceAseem.error
	async def AseemError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = "announceSia")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceSia(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Sia Mulge", "Those Youth Terms", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&835804110786658305> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceSia.error
	async def SiaError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = "announceVanshaj")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceVanshaj(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Vanshaj", "Internet Psychology 101", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&835804105275736134> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceVanshaj.error
	async def VanshajError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = "announceSid")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceSid(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Sid Park", "Startups ki Saanp Seedhi", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&835804112863494186> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceSid.error
	async def SidError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = "announceViraj")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceViraj(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Viraj Raundal", "Observe: Tech and all the stuff around it!", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&829296550601031710> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceViraj.error
	async def VirajError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = "announceHarish")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceHarish(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Curious Harish", "Creator Club", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&829295982453194772> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceHarish.error
	async def HarishError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = "announceSakshi")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceSakshi(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Sakshi Soni", "The Quintessential Queens", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&838413457623744542> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceSakshi.error
	async def SakshiError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = "announceYogen")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceYogen(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Yogen", "Influenced Consumer", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&838413807435907083> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceYogen.error
	async def YogenError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = "announceGargi")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceGargi(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Gargi", "The Garspective Show : Understanding Within and Beyond", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&838414123514986556> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceGargi.error
	async def GargiError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = "announceStress")
	@commands.has_any_role(742028591281340557, 754760818289279057, 835850188827394058)
	async def announceStress(self, ctx, *, PodcastTopic):
		PodcastEmbed = await self.AnnouncementEmbed("Deshna and Tanisha", "Successfully Stressed", PodcastTopic)
		#await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&782495306021470238>')
		await self.client.get_channel(self.AnnouncementChannelID).send(f'<@&780394943302074388> <@&838414286609973248> https://discord.gg/jAjNZ9TMK7', embed = PodcastEmbed)
	@announceStress.error
	async def StressError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
def setup(client):
	client.add_cog(Announcements(client))
