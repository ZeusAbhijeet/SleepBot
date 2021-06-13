# BlueLearn's SleepBot

Official Bot for the Bluelearn.in Discord Server written in Python using Discord.py

Though this bot is intended to be used only on the BlueLearn Discord Server, you can self host it in your server to test it out. Installation guide down below.

## Dependancies

This bot requires the [Discord.py v1.5+ library](https://discordpy.readthedocs.io/), [pretty-help 1.1.2](https://pypi.org/project/discord-pretty-help/), [discord-py-slash-command 1.1.0](https://pypi.org/project/discord-py-slash-command/), [dpytools](https://github.com/chrisdewa/dpytools) and [dpymenus 1.2](https://pypi.org/project/dpymenus/) which can be installed using pip package manager.

## How to host the bot

1. Edit the i-channel_table.txt file in SQL_CMDS folder as required.
2. Run the SQLite3_Py.py script to make the database file.
3. Create a .env file in the same directory as Main.py and enter your Discord Bot Token like this:

```py
DISCORD_TOKEN=Your Token Here
```

4. Run Main.py to start the bot!

## Note

This bot requires Server Members Intent so make sure to enable that by going to your Discord Application -> Bot -> Privilaged Gateway Intents and enabling Server Members Intent. Without this, bot won't be able to access the cache to get user names.

## Contribution

Pull Requests will no longer be accepted on this repository. To create a pull request, go to the following repo: https://github.com/Clinify-Open-Sauce/SleepBot. However, this repository will continue to be updated.

## Changelogs

13 June 2021:

Added new command: study_buddies

21 May 2021:

1. Changed Ping command
2. Added slowmode command (requires [dpytools](https://github.com/chrisdewa/dpytools) for some checks and conversion to timedelta)
3. A few other minor changes

03 May 2021 (Another Update):

Errors now show up in chat instead of console.

03 May 2021:

1. Update Welcome.py
2. Add Announcements.py

01 May 2021:

Fix Welcome.py

29 Apr 2021:

1. Added Forest.py
2. Integrate ClinifyForest API (Credits: [tiluckdave](https://github.com/tiluckdave))

29 Mar 2021:

1. Added Study.py
2. Added Welcome.py
3. Added new Slash Commands

27 Jan 2021:

This changelog contains changelog of a few previous commits that I forgot to document because I am too lazy.

1. Fix an issue wherein ?ask would not work if there is only one result (Credits: [YogPanjarale](https://github.com/YogPanjarale)).
2. Add `intent.guilds`.
3. Changes to rule_begins command.
4. Removed ability to fetch other user's avatar due to complaints from users.

30 Dec 2020:

Probably the last update of the year.

1. Added new cog: Rule.
2. Added new command: rule_begins.
3. rule_lookup has now been added to Rule cog instead.

29 Dec 2020:

1. Added alias for top command: 'lb'.
2. 'top' command no longer shows users who have left the server.

13 Dec 2020:

1. 'ask' and 'howtoask' commands now use menus to display multiple items.
2. Fixed typos in 'ask' command.

12 Dec 2020:

1. Added new command 'ask' (Contributed by [YogPanjarale](https://github.com/YogPanjarale)).

07 Dec 2020:

1. Removed .s as a prefix.

2. Added top command. Use top instead to view the leaderboards.

06 Dec 2020:

1. Bot will now ping the user you mention after running "howtoask" and "beforeyouask" commands.

04 Dec 2020:

1. Added "howtoask" and "beforeyouask" commands (Recommended by [Zircoz](https://github.com/Zircoz))

03 Dec 2020:

1. Added "Flip a Coin" command (Contributed by [parthivpatel1106](https://github.com/parthivpatel1106)).

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
