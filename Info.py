import discord
import random

from discord import colour
import Util
import sqlite3
from dpymenus import Page, PaginatedMenu
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand

class Info(commands.Cog):
	"""
	Contains commands giving information about bot's latency and about the bot
	"""
	def __init__(self, client):
		self.client = client

	guild_ids = Util.guild_ids
	
	@cog_ext.cog_slash(name='ping', description="Pong! Shows the latency of the bot")
	async def _ping(self, ctx):
		ping_embed=discord.Embed(title='Pong!', 
			description=f'Ping = {round(self.client.latency * 1000)}ms', 
			colour=random.randint(0,0xffffff)
		)
		ping_embed.set_footer(text=f'Requested by {ctx.author}')
		await ctx.send(embed=ping_embed)
	
	@commands.command(name='ping', aliases=['latency'], help='Pong!')
	async def ping(self, ctx):
		#loading_embed = discord.Embed(description="loading...")
		msg = await ctx.send(embed = Util.loading_embed)
		latency_ms = round((msg.created_at.timestamp() - ctx.message.created_at.timestamp()) * 1000, 1)
		heartbeat_ms = round(ctx.bot.latency * 1000, 1)
		await msg.edit(embed=discord.Embed(title='Pong!', 
						description=f"Latency: `{latency_ms}ms`\nHeartbeat: `{heartbeat_ms}ms`\n\nThis isn't important to you tho",
						colour=random.randint(0, 0xffffff)))
	
	@commands.command(name='howtoask', help='Gives an explanation on how to ask a question')
	async def howtoask(self, ctx, page = 0, target: discord.Member = None):
		embedcolour = random.randint(0, 0xffffff)
		helpEmbed = discord.Embed(title = "How to ask",
				description = "Here is a short explanation on how you should ask a question efficiently:",
				colour = embedcolour
		)
		helpEmbed.set_thumbnail(url="https://res.cloudinary.com/zeusabhijeet/image/upload/v1607099122/SleepBot/Info%20Commands/ask_question.png")
		if target != None:
			helpEmbed.set_author(name=target, icon_url=target.avatar_url)
		else:
			helpEmbed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
		helpEmbed.add_field(name="No Hello",
			value="It's alright if you don't greet. You can directly ask your question right away; it saves your's and the other person's time. More on that [here](https://www.nohello.com/).",
		)
		helpEmbed1 = discord.Embed(title = "Asking a Code Related Question",
			description="""To ask a question on a code, refrain from sending screenshots or photos of the code as they are usually barely visible.
			Here are two ways you can share your code:""",
			colour = embedcolour)
		helpEmbed1.set_thumbnail(url='https://res.cloudinary.com/zeusabhijeet/image/upload/v1607100500/SleepBot/Info%20Commands/howtoask_code.png')
		helpEmbed1.add_field(name="1. Use an Online Code Sharing Service",
			value="""
				Use these if the code you are sharing is larger than 12 lines.
				Below are some of the code sharing services that you can use: 
				[GitHub Gist](https://gist.github.com/), [JSfiddle](https://jsfiddle.net/), [Codepen](https://codepen.io/),	
				[Pastebin](https://pastebin.com/), [OnlineGDB](https://www.onlinegdb.com/), [repl.it](https://repl.it/), etc""",
			inline = False)
		helpEmbed1.add_field(name="2. Use a Code Snippet",
			value="""Use these when the code you are sharing is less than or about 12 lines.
				To make a code snippet, encase your code between a pair of 3 backticks
				
				\```
				Like This
				\```
				
				So when a code is sent, it will look something like this:
```py
# python3 Hello World Program
print("Hello World!")
```

				You can read more about how Discord's Markdown works [here](https://gist.github.com/matthewzring/9f7bbfd102003963f9be7dbcf7d40e51).""",
			inline = False)
		if target != None:
			helpEmbed1.set_author(name=target, icon_url=target.avatar_url)
		else:
			helpEmbed1.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
		if target != None:
			await ctx.send("<@!{}>".format(target.id))
		if page == 1:
			await ctx.send(embed = helpEmbed)
		elif page == 2:
			await ctx.send(embed = helpEmbed1)
		else:
			menu = PaginatedMenu(ctx)
			menu.add_pages([helpEmbed, helpEmbed1])
			menu.set_timeout(30)
			menu.show_command_message()
			menu.persist_on_close()
			menu.show_page_numbers()
			menu.allow_multisession()
			await menu.open()
	
	@commands.command(name='beforeyouask', help="Gives an explanation on what to do before asking a question")
	async def beforeyouask(self, ctx, target: discord.Member = None):
		embed = discord.Embed(title = "Before You Ask",
			description = "Before you ask a question, make sure you do the following:",
			colour = random.randint(0, 0xffffff)
		)
		if target != None:
			embed.set_author(name=target, icon_url=target.avatar_url)
		else:
			embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
		embed.add_field(name="Check the pinned messages", 
			value="The pinned messages contain some instructions on how to ask your question. They can also possibly contain a solution to your problem already.",
			inline=False
		)
		embed.add_field(name="Do a Google Search",
			value="Many times, solution is just a search away on Google; it will save other's time and yours too.",
			inline=False
		)
		embed.add_field(name="Search your problem on fourm websites",
			value="""Common problems are mostly solved on sites like [StackOverflow](https://stackoverflow.com/) or [GeeksForGeeks](https://www.geeksforgeeks.org/). Do check them out before asking here.""",
			inline=False
		)
		embed.add_field(name="Bonus: Rubber Duck Debugging",
			value="""When you are learning something new and/or complex, your mind might get overloaded with information and you may not see the obvious solution. 
			Then write down your problem from the basic, and you might help yourself before others do. More on it [here](https://blog.codinghorror.com/rubber-duck-problem-solving/).
			
			If you still haven't found any solution to your problem, you are free to go ahead and ask. Do run the ?howtoask command to get instructions on how to ask your question.""",
			inline=False
		)
		embed.set_footer(text="Embed 1 of 1")
		if target != None:
			await ctx.send("<@!{}>".format(target.id))
		await ctx.send(embed = embed)

	@cog_ext.cog_slash(name='about', description="Gives info about SleepBot")
	async def _about(self, ctx):
		aboutEmbed = discord.Embed(title = "About SleepBot",
			description="SleepBot is a custom coded and open source bot made by [ZeusAbhijeet](https://github.com/ZeusAbhijeet/) for [Bluelearn.in](https://www.bluelearn.in/) Discord Server. It is written in Python and uses discord.py library.", 
			colour = random.randint(0, 0xffffff))
		aboutEmbed.set_thumbnail(url='https://res.cloudinary.com/zeusabhijeet/image/upload/v1607093923/SleepBot/Info%20Commands/SleepBot_Image.png')
		aboutEmbed.add_field(name="Contributors!",
			value="""**Thank you to the following people for contributing:**
				1. [itsCharmander](https://github.com/itsCharmander)\n2. [AryaKesharwani](https://github.com/AryaKesharwani)
				3. [parthivpatel1106](https://github.com/parthivpatel1106)\n4. [Zircoz](https://github.com/Zircoz)
				5. [YogPanjarale](https://github.com/YogPanjarale)\n6. [AmayWale](https://github.com/AmeyWale)
				7. [tiluckdave](https://github.com/tiluckdave)""",
			inline=False
		)
		aboutEmbed.add_field(name="Contribute to SleepBot!", 
			value="SleepBot is an Open Source bot with it's source code available [here](https://github.com/ZeusAbhijeet/SleepBot). You are free to contribute to it!",
			inline=False
		)
		await ctx.defer()
		await ctx.send(embed=aboutEmbed)
	

	@commands.command(name='about', help='About the bot!')
	async def about(self, ctx):
		aboutEmbed = discord.Embed(title = "About SleepBot",
			description="SleepBot is a custom coded and open source bot made by [ZeusAbhijeet](https://github.com/ZeusAbhijeet/) for [Bluelearn.in](https://www.bluelearn.in/) Discord Server. It is written in Python and uses discord.py library.", 
			colour = random.randint(0, 0xffffff))
		aboutEmbed.set_thumbnail(url='https://res.cloudinary.com/zeusabhijeet/image/upload/v1607093923/SleepBot/Info%20Commands/SleepBot_Image.png')
		aboutEmbed.add_field(name="Contributors!",
			value="""**Thank you to the following people for contributing:**
				1. [itsCharmander](https://github.com/itsCharmander)\n2. [AryaKesharwani](https://github.com/AryaKesharwani)
				3. [parthivpatel1106](https://github.com/parthivpatel1106)\n4. [Zircoz](https://github.com/Zircoz)
				5. [YogPanjarale](https://github.com/YogPanjarale)\n6. [AmayWale](https://github.com/AmeyWale)
				7. [tiluckdave](https://github.com/tiluckdave)""",
			inline=False
		)
		aboutEmbed.add_field(name="Contribute to SleepBot!", 
			value="SleepBot is an Open Source bot with it's source code available [here](https://github.com/Clinify-Open-Sauce/SleepBot). You are free to contribute to it!",
			inline=False
		)
		aboutEmbed.set_footer(text="Requested by {}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=aboutEmbed)
	
	@commands.command(name="?", aliases = ['??', '???', '????'])
	async def questionmark(self, ctx):
		pass


def setup(client):
	client.add_cog(Info(client))
