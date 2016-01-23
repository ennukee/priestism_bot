# Priestism Bot

A bot designed solely for the purpose of my own Discord server. If you wish to use this, there will be a **lot** of things you'll need to modify.

The first versions of this bot (up to 0.3.X or so) was created within a few days of learning Python. Anything prior to a public version (1.0.0) will be amateur-style coding that I write while learning conventions and efficiency maximization. There may (*will*) be inefficient code here, but as I learn the language more, I plan to fix the inefficiencies and further improve my code in the future. Some of the basic stuff you must do are as following:

 1. Log-in info. Create a 'login.txt' file and put the email first, followed by a space, then the password (note: password cannot have any spaces)
 2. Create a 'server log' text channel. Go into and use the '!channelid' command to find the ID. Replace the existing number (at the top of the python file) with the server log ID.
 3. Repeat #2 for your 'General chat' for the bootup sequence

I don't provide any technical support for this bot. There's far too much that is hardcoded for it to easily work on anyone's system. If you know what you're doing, you can probably get it working. It probably isn't worth the time otherwise though. I'll likely abstract it before its public release version, but that's far, *far* into the future.

# Priestism Bot Command Info
(only includes commands usable by the general users, parse the source code for the admin restricted commands)

Commands:
```python
!name
!id
!serverid

!say MESSAGE
!armory CHARACTER_NAME REALM_NAME (include spaces)
!twitch TWITCH_CHANNEL_NAME
!tokens

KappaRoss
WutFace
BabyRage

!whois NAME
!setwhois 
# note, the above will prompt you for your bio, don't include in the name

!osu user NAME 
!osu compare NAME1 NAME2
!osu bestof NAME [num]
!osu recent NAME [num]

!addgame
# will add a role to your role list if you're currently in a supported game

!mmo create CHARACTER_NAME
!mmo explore
!mmo stats [CHARACTER_NAME]
!mmo backpack

!game guess X # guessing game from 0 to X
!game guess rules
!game guess leaderboard

!game math number_of_values [max_value, timeout]
e.g. !game math 3 20 10
```
How are you
Do you love me
I love you
How loved are you
```

Known bugs:
 * Only logs edits/deletes if the message was created during the bot's current session

# TO-DO
```
 TODO:
 * finish !mmo explore
 * add !mmo crafting
 * add !mmo delete
 * update current command syntax to the new format supported by 0.10.0 (from the 0.9.1 used now)
 ```

# Changelog
```
Update 0.46

 * added !osu recent NAME which will view the 5 recent plays by NAME (can specify an additional parameter to go up to 10)
 * added !osu bestof NAME which will view the 5 best pp gains by NAME (can specify an additional parameter to go up to 10)

Update 0.4.3
"osu! API and !addgame"

 * Begun integration of the osu! API into the bot. Current commands: !osu user NAME which will load their stats, !osu compare NAME1 NAME2 which will compare two users' stats
 * !addgame will now add a game to your role if it is an existing game role

Update 0.4.2c (beta)
"QoL updates"

 * added a !reload command, allowing the script admin to modify the script, then run this command in order to reload the script without the need to manually close and re-open the script
 * added the !say command, allowing you to tell Priestism Bot to say whatever you'd like (deletes the message afterward)

Update 0.4.2 (beta)
"Actual MMO Update!"

 * added backpack integration
 * added item discovery in !mmo explore (10% chance)
 * added !mmo backpack to view your backpack

Update 0.4.1 (beta)
"The Not-Actually-A-MMO-Update Update"

 * added the !avatar command
 * view anyone's avatar by typing !avatar followed by their name (i.e. !avatar enragednuke) or view everyone's avatar by typing !avatars (disable this in large servers)
 * added the !mal command
 * generate a link to anyone's MAL profile or list by typing the !mal command followed by their MAL name (if linking to list, type !mal list THEN their name, so for example !mal list enragednuke)

Update 0.4.0a (beta)

 * added a !eval command
 * type any mathematical equation following !eval and Priestism Bot will do it for you (it actually runs any valid python code) but due to how much it can breach security of the code, it's restricted to admin-level access only

Update 0.4.0 (beta)
"The start of the 'PriestMMO' updates"

 * Added the new !mmo command
 * The following commands are valid: !mmo create, !mmo stats PLAYERNAME (you can do just !mmo stats to view your own stats), and !mmo explore
 * !mmo explore is currently not implemented

Update 0.3.3a

 * Added !cmds command to view a list of all custom-made commands

Update 0.3.3
The 'Custom Commands & Administration' update

 * added commands +cmd and -cmd to add and remove custom commands
 * added ability to restrict commands (only command generation and bot affection are restricted) through an admin list (can add and remove via +admin and -admin, view all admins by using !admins)
 * fixed file structure

Update 0.2.4
The 'Who is?' update

* added !whois and !setwhois commands
* removed the greeting spam on bot bootup
* now tracks version and build number
```
