# Priestism Bot

A bot designed solely for the purpose of my own Discord server. If you wish to use this, there will be a **lot** of things you'll need to modify.

The first versions of this bot (up to 0.3.X or so) was created within a few days of learning Python. There may be inefficient code here, but as I learn the language more, I plan to fix the inefficiencies and further improve my code in the future. Some of the basic stuff you must do are as following:

 1. Log-in info. Create a 'login.txt' file and put the email first, followed by a space, then the password (note: password cannot have any spaces)
 2. Create a 'server log' text channel. Go into and use the '!channelid' command to find the ID. Replace the existing number (at the top of the python file) with the server log ID.
 3. Repeat #2 for your 'General chat' for the bootup sequence

I don't provide any technical support for this bot. There's far too much that is hardcoded for it to easily work on anyone's system. If you know what you're doing, you can probably get it working. It probably isn't worth the time otherwise though.

# Priestism Bot Command Info
(only includes commands usable by the general users, parse the source code for the admin restricted commands)

Commands:
```python
!name
!id
!serverid

!armory CHARACTER_NAME REALM_NAME (include spaces)
!twitch TWITCH_CHANNEL_NAME
!tokens

KappaRoss
WutFace
BabyRage

!whois NAME
!setwhois 
# note, the above will prompt you for your bio, don't include in the name

!game guess X # guessing game from 0 to X
!game guess rules
!game guess leaderboard

!game math number_of_values [max_value, timeout]
e.g. !game math 3 20 10
```

For the math game,
!game math 3 could return `3*3-2` and !game math 4 could return `4-2+3*1`
max_value will change the default max of the values of 9 in the equation to whatever you set it to
timeout will change the default solving timeout of 10s to whatever you specify

You can also talk with Priestism Bot by typing 'Priestism Bot' then saying one of these commands:
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
