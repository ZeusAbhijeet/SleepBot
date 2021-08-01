from convertors.humanreadabletime import handleError
import discord
from discord.ext import commands
import asyncio
import os
import random
# For Database related stuff
import sqlite3
from dotenv import load_dotenv
from datetime import datetime
from datetime import date


POINT = {}

# Open and connect to Database File
conn = sqlite3.connect('Database.db')
c = conn.cursor()

c.execute("SELECT channel_ID FROM channel_table WHERE title='LOG';")
LOG = c.fetchone()
c.execute("SELECT user_id, points FROM point_table;")
DB_POINT = c.fetchall()
c.execute("SELECT channel_ID FROM channel_table WHERE title='POINT';")
POINTCMD = c.fetchone()
c.execute("SELECT channel_ID FROM channel_table WHERE title='RULE';")
RULE_CHNL = c.fetchone()
c.execute("SELECT channel_ID FROM channel_table WHERE title='POINT-EARN-CHANNEL';")
POINT_EARN_CHNLS = c.fetchall()

POINTCMD = int(POINTCMD[0])
RULE_CHNL = int(RULE_CHNL[0])

loading_embed = discord.Embed(description="<a:bot_loading:809318632723185714> loading...")

guild_ids = [740589508365385839]

GUILD_ID = 740589508365385839

def is_point_cmd_chnl():
    def predicate(ctx):
        return int(ctx.channel.id) == int(POINTCMD)
    return commands.check(predicate)

def is_rule_chnl(ctx):
	return int(ctx.channel_id) == int(RULE_CHNL)

def is_point_chnl(ctx):
	for channel in POINT_EARN_CHNLS:
		if int(channel[0]) == int(ctx.channel.id):
			return True
	return False

conn.close()

async def ErrorHandler(ctx, error):
	ErrorEmbed = discord.Embed(title = "An Error Occured :(",
								description = "The command could not be run.",
								colour = discord.Colour.red())
	ErrorEmbed.add_field(name= "Reason :", value="{}".format(handleError(error)), inline = False)
	ErrorEmbed.add_field(name="What to do now?", value= "Try running the command again or report this to <@!515097702057508882>.", inline = False)
	ErrorEmbed.set_thumbnail(url="https://res.cloudinary.com/zeusabhijeet/image/upload/v1620057874/SleepBot/Errors/Error.png")
	await ctx.send(f':no_entry_sign: **ERROR** :no_entry_sign:', embed = ErrorEmbed)

# For Backup to Database
async def Backup(client):
	await client.wait_until_ready()
	global POINT
	global DB_POINT
	while not client.is_closed():
		await client.get_channel(LOG[0]).send(f"Backup OK: ```{datetime.now()}```")
		# Repeat every 1 hour
		await asyncio.sleep(1800)
		conn = sqlite3.connect('Database.db')
		c = conn.cursor()

		c.execute("SELECT user_id, points FROM point_table;")
		DB_POINT = c.fetchall()

		await client.get_channel(int(LOG[0])).send(f"Performing Backup: ```{datetime.now()}```")
		# POINT BACKUP
		for user in DB_POINT:
			if user[0] in POINT:
				c.execute("UPDATE point_table SET points = {} WHERE user_ID = {}".format(POINT[user[0]]+user[1],user[0]))
		is_instance = False
		for user in POINT:
			for elm in DB_POINT:
				if user in elm:
					is_instance = True
					break
			if not is_instance:
				c.execute("INSERT INTO point_table VALUES (NULL, {}, {});".format(user,POINT[user]))
			is_instance = False
		
		c.execute("SELECT user_ID, points FROM point_table;")
		DB_POINT = c.fetchall()

		conn.commit()
		conn.close()

		POINT = {}

# Function to log commands
async def command_log(client, ctx, cmd_name):
	embed = discord.Embed(
		title = "SleepBot Command Logs",
		description = ("Command: {}\nMessage Content: {}".format(cmd_name, ctx.message.content)),
		colour = random.randint(0, 0xffffff)
	)
	embed.add_field(name = "In Guild:", value = "{}".format(ctx.guild), inline = False)
	embed.add_field(name = "In Channel:", value = "{} Channel_ID: {}".format(ctx.channel, ctx.channel.id), inline = False)
	embed.add_field(name = "Author:", value = "{}, Nick: {}, ID: {}".format(ctx.author, ctx.author.nick, ctx.author.id), inline = False)
	embed.add_field(name = "Time:", value = "{}".format(datetime.now()), inline = False)

	await client.get_channel(LOG[0]).send(embed = embed)
