import discord
from discord.ext import commands
import asyncio
import os
import sqlite3

POINT = {}

conn = sqlite3.connect('Database.db')
c = conn.cursor()

c.execute("SELECT user_id, points FROM point_table")
DB_POINT = c.fetchall()

conn.close()

