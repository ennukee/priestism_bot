# Priestism Bot

A bot designed solely for the purpose of my own Discord server. If you wish to use this, there will be a lot of things you'll need to modify.

 1. Log-in info. Create a 'login.txt' file and put the email first, followed by a space, then the password (note: password cannot have any spaces)
 2. Create a 'server log' text channel. Go into and use the '!channelid' command to find the ID. Replace the existing number (at the top of the python file) with the server log ID.
 3. Repeat #2 for your 'General chat' for the bootup sequence

I don't provide any technical support for this bot.

Changelog
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
