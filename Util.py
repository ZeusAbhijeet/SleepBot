import discord
from discord.ext import commands
import asyncio
import os
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

conn.close()

# For Backup to Database
async def Backup(client):
	await client.wait_until_ready()
	global POINT
	global DB_POINT
	while not client.is_closed():
		await client.get_channel(LOG).send(f"Backup OK: {datetime.now()}")
		# Repeat every 1 hour
		await asyncio.sleep(3600)
		conn = sqlite3.connect('Database.db')
		c = conn.cursor()

		c.execute("SELECT user_id, points FROM point_table;")
		DB_POINT = c.fetchall()

		await client.get_channel(LOG).send(f"Performing Backup: ```{datetime.now()}```")
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
		
		conn.commit()
		conn.close()

		POINT = {}

