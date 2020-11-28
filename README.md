# Clinify Squad's SleepBot
Official Bot for the Clinify.in Discord Server written in Python using Discord.py

Though this bot is intended to be used only on the Clinify.in Discord Server, you can self host it in your server to test it out. Installation guide down below.

## Dependancies
This bot requires the [Discord.py v1.5+ library](https://discordpy.readthedocs.io/) and [pretty-help 1.1.2](https://pypi.org/project/discord-pretty-help/) which can be installed using pip package manager.

## How to host the bot
1. Edit the i-channel_table.txt file in SQL_CMDS folder as required.
2. Run the SQLite3_Py.py script to make the database file.
3. Create a .env file in the same directory as Main.py and enter your Discord Bot Token like this:
```
DISCORD_TOKEN=Your Token Here
```
4. Run Main.py to start the bot!

## Note
This bot requires Server Members Intent so make sure to enable that by going to your Discord Application -> Bot -> Privilaged Gateway Intents and enabling Server Members Intent. Without this, bot won't be able to access the cache to get user names.

## Changelogs
28 Nov 2020:
1. Using PrettyHelp as default help command.
2. Added Avatar command to show the avatar of mentioned user.
3. Added an About command.
4. Added a new prefix '?'.

08 Nov 2020:
1. Restricted points command to one channel. Running it in any other channel will show an error.
2. Added new alises for points and give_points commands
3. Added command logging. Bot will now send a message in the log channel with details about the command, the message content, message author, etc.

## Upcoming Changes
1. Transition to MongoDB.
2. Add command to share coins with other users

## Credits
This bot contains code from the following Repos:
1. [Robobert](https://github.com/JTexpo/Robobert): For the Point.py, Util.py and SQL_CMDS

Special Thanks to [JTexpo](https://github.com/JTexpo) for helping me make this bot and letting me use parts of his code.
