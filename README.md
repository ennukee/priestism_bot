# Priestism Bot

A bot designed solely for the purpose of my own Discord server. If you wish to use this, there will be a lot of things you'll need to modify.

The first versions of this bot (up to 0.3.X or so) was created within a few days of learning Python. There may be inefficient code here, but as I learn the language more, I plan to fix the inefficiencies and further improve my code in the future.

 1. Log-in info. Create a 'login.txt' file and put the email first, followed by a space, then the password (note: password cannot have any spaces)
 2. Create a 'server log' text channel. Go into and use the '!channelid' command to find the ID. Replace the existing number (at the top of the python file) with the server log ID.
 3. Repeat #2 for your 'General chat' for the bootup sequence

I don't provide any technical support for this bot.

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

# Changelog
```
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
