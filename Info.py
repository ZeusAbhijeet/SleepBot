import discord
import random
from discord.ext import commands

class Info(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name='ping', aliases=['latency'], help='Pong!')
	async def ping(self, ctx):
		embed=discord.Embed(title='Pong!', 
			description=f'Ping = {round(self.client.latency * 1000)}ms', 
			colour=random.randint(0,0xffffff)
		)
		embed.set_footer(text=f'Requested by {ctx.author}')
		await ctx.send(embed=embed)
	
	@commands.command(name='howtoask', help='Gives an explaination on how to ask a question')
	async def howtoask(self, ctx):
		embedcolour = random.randint(0, 0xffffff)
		helpEmbed = discord.Embed(title = "How to ask",
				description = "Here is a short explaination on how you should ask a question so that people are more likely to help you out:",
				colour = embedcolour
		)
		helpEmbed.set_thumbnail(url="https://res.cloudinary.com/zeusabhijeet/image/upload/v1607099122/SleepBot/Info%20Commands/ask_question.png")
		helpEmbed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
		helpEmbed.add_field(name="No Hello",
			value="It's alright if you don't greet. You can directly ask your question right away. Saves your's and the other person's time. More on that [here](https://www.nohello.com/).",
		)
		helpEmbed.set_footer(text="Embed 1 of 2")
		helpEmbed1 = discord.Embed(title = "Asking a Code Related Question",
			description="""To ask a question on a code, refrain from sending screenshots or photos of the code as they are usually barely visible.
			Here are two ways you can share your code:""",
			colour = embedcolour)
		helpEmbed1.set_thumbnail(url='https://res.cloudinary.com/zeusabhijeet/image/upload/v1607100500/SleepBot/Info%20Commands/howtoask_code.png')
		helpEmbed1.add_field(name="1. Use an Online Code Sharing Service",
			value="""
				Below are some of the code sharing services that you can use: 
				1. [GitHub Gist](https://gist.github.com/) 
				2. [JSfiddle](https://jsfiddle.net/) 
				3. [Codepen](https://codepen.io/) 
				4. [Pastebin](https://pastebin.com/)
				5. [OnlineGDB](https://www.onlinegdb.com/)
				6. [repl.it](https://repl.it/)""",
			inline = False)
		helpEmbed1.add_field(name="2. Use a Code Snippet",
			value="""To make a code snippet, encase your code between a pair of 3 backticks
				
				\```
				Like This
				\```
				
				So when a code is sent, it will look something like this:
```cpp
// C++ Hello World Program
#include <iostream>
using namespace std;
int main() {
	cout << 'Hello World!';
	return 0;
}
```

				You can read more about how Discord's Markdown works [here](https://gist.github.com/matthewzring/9f7bbfd102003963f9be7dbcf7d40e51).""",
			inline = False)
		helpEmbed1.set_footer(text="Embed 2 of 2")
		await ctx.send(embed = helpEmbed)
		await ctx.send(embed = helpEmbed1)

	@commands.command(name='about', help='About the bot!')
	async def about(self, ctx):
		aboutEmbed = discord.Embed(title = "About SleepBot",
			description="SleepBot is a custom coded and open source bot made by [ZeusAbhijeet](https://github.com/ZeusAbhijeet/) for Clinify.in Discord Server. It is written in Python and uses discord.py library.", 
			colour = random.randint(0, 0xffffff))
		aboutEmbed.set_thumbnail(url='https://res.cloudinary.com/zeusabhijeet/image/upload/v1607093923/SleepBot/Info%20Commands/SleepBot_Image.png')
		aboutEmbed.add_field(name="Contribute to SleepBot!", 
			value="SleepBot is an Open Source bot with it's source code available [here](https://github.com/ZeusAbhijeet/SleepBot). You are free to contribute to it!",
			inline=False
		)
		aboutEmbed.add_field(name="Contributors!",
			value="""**Thank you to the following people for contributing:**
				1. [itsCharmander](https://github.com/itsCharmander)\n2. [AryaKesharwani](https://github.com/AryaKesharwani)
				3. [parthivpatel1106](https://github.com/parthivpatel1106)""",
			inline=False
		)
		aboutEmbed.set_footer(text="Requested by {}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=aboutEmbed)
		

def setup(client):
	client.add_cog(Info(client))
