import discord
from discord.ext import commands
import asyncio
import sqlite3
import random
import Util

class Rule(commands.Cog):
	"""
	Contains command for looking up a rule with it's index value
	"""
	def __init__(self, client):
		self.client = client
		conn = sqlite3.connect('Database.db')
		c = conn.cursor()
		self.roles = c.execute("SELECT role_ID FROM role_table WHERE title = 'RULE';").fetchone()
		self.roles = int(self.roles[0])
		conn.close()

	@commands.command(name = 'rule_lookup',
						aliases = ['rule'],
						help = "Brings up the mentioned rule clause for quick reference.")
	async def rule_lookup(self, ctx, rule = 1):
		await Util.command_log(self.client,ctx,"rule_lookup")
		conn = sqlite3.connect('Database.db')
		c = conn.cursor()
		rule = c.execute("SELECT * FROM rule_table WHERE db_ID = {};".format(rule)).fetchone()
		conn.close()
		msg = await ctx.send(embed = Util.loading_embed)
		await msg.edit(embed = discord.Embed(title = "{} Pulled Up A Rule As A Quick Reference!".format(ctx.author.name),
			description = "**{}.** {}".format(rule[0],rule[1]),
			colour = random.randint(0,0xffffff)))
	@rule_lookup.error
	async def ruleError(self, ctx, error):
		await Util.ErrorHandler(ctx, error)
	
	@commands.command(name = 'rule_begins',
				aliases = ['rule_begin','rb'])
	@commands.has_permissions(administrator=True)
	async def rule_begins(self, ctx):
		await Util.command_log(self.client,ctx,"rule_begins")
		chnl = self.client.get_channel(Util.RULE_CHNL)
		color = random.randint(0,0xffffff)
		conn = sqlite3.connect('Database.db')
		c = conn.cursor()
		rules = c.execute("SELECT * FROM rule_table;").fetchall()
		conn.close()
		rule_message = """
Welcome to the **__BlueLearn Discord Server__**! Enjoy your time here and make sure to read the rules carefully.
Please read and abide by the Discord ToS/Guidelines. Breaking these will result in an immediate ban
Discord ToS: https://discord.com/guidelines \n
**Server Rules:**"""
		rule_message2 = ""
		rule_message3 = ""
		for rule in range(0,7):
			rule_message += "\n**{}.** {}".format(rules[rule][0],rules[rule][1])
		msg = await chnl.send(embed = discord.Embed(title = "React To This Message To Show You've Read The Rules!",
                description = rule_message,
                colour = color)
                )
		for rule in range(7,15):
			rule_message2 += "\n**{}.** {}".format(rules[rule][0],rules[rule][1])
		msg = await chnl.send(embed = discord.Embed(
                description = rule_message2,
                colour = color)
                )
		for rule in range(15,len(rules)):
			rule_message3 += "\n**{}.** {}".format(rules[rule][0],rules[rule][1])
		rule_message3 += """

**Punishments :**
  __3 Warns__ : 6 hour mute.
  __4 Warns__ : Kick.
  __8 Warns__ : Ban.
  
**To clarify what spam means :**
Sending 5 or more messages that are repeated or do not contribute to the conversation can be flagged as spam. Sending emotes is fine but sending singular emotes continuously 4 times in a row can be considered spam.

"""

		msg = await chnl.send(embed = discord.Embed(
                description = rule_message3,
                colour = color)
                )
		await msg.add_reaction("\U0001F4DD")
	
	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
		if not Util.is_rule_chnl(payload):
			return
		if payload.user_id == self.client.user.id:
			return
		else:
			user = await self.client.get_guild(740589508365385839).fetch_member(payload.user_id)
			await user.add_roles(self.client.get_guild(740589508365385839).get_role(self.roles))

def setup(client):
	client.add_cog(Rule(client))
