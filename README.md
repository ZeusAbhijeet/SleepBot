# Clinify Squad's SleepBot
Official Bot for the Clinify.in Discord Server written in Python using Discord.py

Though this bot is intended to be used only on the Clinify.in Discord Server, you can self host it in your server to test it out. Installation guide down below.

## Dependancies
This bot requires the Discord.py library which can be installed using pip package manager.

## How to host the bot
1. Edit the i-channel_table.txt file in SQL_CMDS folder as required.
2. Run the SQLite3_Py.py script to make the database file.
3. Create a .env file in the same directory as Main.py and enter your Discord Bot Token like this:
```
DISCORD_TOKEN=Your Token Here
```
4. Run Main.py to start the bot!

## Credits
This bot contains code from the following Repos:
[Robobert](https://github.com/JTexpo/Robobert): For the Point.py, Util.py and SQL_CMDS

Special Thanks to [JTexpo](https://github.com/JTexpo) for helping me make this bot and letting me use parts of his code.
