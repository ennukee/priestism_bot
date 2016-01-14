# encoding: utf-8
import discord
import asyncio
import random
import codecs
import datetime
import os

client = discord.Client()
log_server = discord.Object(133761409929576449)
main_server = discord.Object(126122560596213760)
local_ilys = 0
version = "0.4.2 (beta)"
subtitle = "The PriestMMO Update (Beta)"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ON_READY EVENT #

@client.async_event
def on_ready():
	global version
	build_up()
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	#d_view = [ (v,k) for k,v in dic.items() ]
	#d_view.sort(reverse=True)
	yield from client.send_message(main_server, "**Priestism Bot** booting up!\nVersion: *{0} Build {1}*\n*{2}*".format( version, str(builds()), subtitle ))

def build_up():
	num = builds()
	fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/buildcount.txt", "w+")
	fo.write(str(num+1))
	fo.close()

def builds():
	fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/buildcount.txt", "r")
	data = int(fo.read())
	fo.close()
	return data

def admins():
	fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/admins.txt", "r")
	data = fo.read().split('|')
	fo.close()
	return data

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

@client.async_event
def on_message(message):
	global local_ilys
	# TROLL ALEX #
	if str(message.author) == "Spaceman659":
		if random.randrange(19) == 0:
			yield from client.send_message(message.channel, 'got ish kid?', tts=True)
			clog("alex ish success", message.author.name, message.author.id)
		else:
			clog("alex ish fail", message.author.name, message.author.id)

	# MEMES #
	if message.content == "BabyRage":
		yield from client.send_file(message.channel, "C:/Users/Dylan/Documents/discord botts/test1/imgs/BabyRage.png")
	elif message.content == "KappaRoss":
		yield from client.send_file(message.channel, "C:/Users/Dylan/Documents/discord botts/test1/imgs/KappaRoss.png")
	elif message.content == "WutFace":
		yield from client.send_file(message.channel, "C:/Users/Dylan/Documents/discord botts/test1/imgs/WutFace.png")

	elif message.content.lower() == "priestism bot":
		yield from client.send_message(message.channel, "Hello {0}".format(message.author.name))
		i1 = yield from client.wait_for_message(timeout=10.0, author=message.author)
		if i1.content.lower() == "how are you":
			yield from client.send_message(message.channel, "I'm good, thanks")
			pbot_affection(message.author.name, 25)
		elif i1.content.lower() == "i love you":
			yield from client.send_message(message.channel, "<3")
			pbot_affection(message.author.name, 100)
			love_yous(1)
			local_ilys += 1
		elif i1.content.lower() == "do you love me":
			yield from client.send_message(message.channel, {0: "No, I hate you", 1: "No, I'm sorry", 2: "Maybe (*blushes*)", 3: "Maybe (firmly)", 4: "Somewhat", 5: "Yes <3"}[random.randrange(5)+1])
		elif i1.content.lower() == "how loved are you":
			yield from client.send_message(message.channel, "Total: **{0}**\nThis boot-up: **{1}**".format(get_love_yous(), local_ilys))
		else:
			yield from client.send_message(message.channel, "BabyRage")
			yield from client.send_message(message.channel, u"(わかりません, ごめんなさい！！)")

	elif message.content.startswith('+PBOTaff'):
		if message.author.name not in admins():
			yield from client.send_message(message.channel, "Can only be used by an admin")
			return
		params = message.content.split(' ')[1:]
		if len(params)<1:
			yield from client.send_message(message.channel, "Invalid parameters (required: name and realm)")
		if len(params)==1:
			yield from client.send_message(message.channel, "[ADMIN] {0}'s affection: {1}".format(params[0], get_pbot_affection(params[0])))
		else:
			try:		
				pbot_affection(params[0], int(params[1]))
			except IOError as e:
				print("Error({0}): {1}".format(e.errno, e.strerror))
				yield from client.send_message(message.channel, "Error providing {0} {1} affection".format(params[0], params[1]))
			else:
				yield from client.send_message(message.channel, "Successfully granted {0} {1} affection".format(params[0], params[1]))

	# VARIOUS COMMANDS #
	elif message.content.startswith('!name'):
		yield from client.send_message(message.channel, message.author.name)
		clog("!name", message.author.name, message.author.id)
	elif message.content.startswith('!id'):
		yield from client.send_message(message.channel, str(message.author.id))
		clog("!id", message.author.name, message.author.id)
	elif message.content.startswith('!channelid'):
		yield from client.send_message(message.channel, str(message.channel.id))

	elif message.content == "!tokens":
		yield from client.send_message(message.channel, "**Vanquisher** - Rogue, Death Knight, Mage, Druid")
		yield from client.send_message(message.channel, "**Conqueror** - Priest, Paladin, Warlock")
		yield from client.send_message(message.channel, "**Protector** - Warrior, Hunter, Shaman, Monk\n")
		yield from client.send_message(message.channel, "**Hellfire Citadel Tier Drops**\n**Head** - Kormrok\n**Shoulders** - Xhul'horac\n**Chest** - Mannoroth\n**Gloves** - Socrethar\n**Legs** - Gorefiend\n")

	elif message.content.startswith('!avatar'):
		params = message.content.split(' ')[1:]
		if message.content == '!avatars':
			for msg in ["**{0}**'s avatar: `{1}`".format(x.name, x.avatar_url) for x in client.servers[0].members]:
				yield from client.send_message(message.channel, msg)
		elif len(params)==0:
			yield from client.send_message(message.channel, "Invalid number of parameters ({0} for 1)\nUse `!avatars` to view all avatars".format(len(params))) 
		else:
			if ' '.join(params).lower() not in [x.name.lower() for x in client.servers[0].members]:
				yield from client.send_message(message.channel, "{0} is not a valid member of the server".format(' '.join(params)))
			else:
				for msg in ["**{0}**'s avatar: {1}".format(x.name, x.avatar_url) if x.name.lower()==' '.join(params).lower() else None for x in client.servers[0].members]:
					if msg != None:
						yield from client.send_message(message.channel, msg)

	elif message.content.startswith('!mal'):
		params = message.content.split(' ')[1:]
		if len(params)>0 and params[0]=='list':
			name = message.author.name if len(params)==1 else params[1]
			yield from client.send_message(message.channel, "http://myanimelist.net/animelist/{0}".format(name))
		else:
			name = message.author.name if len(params)==0 else params[0]
			yield from client.send_message(message.channel, "http://myanimelist.net/profile/{0}".format(name))

	elif message.content.startswith('!armory'):
		params = message.content.split(' ')[1:]
		if len(params)<2:
			yield from client.send_message(message.channel, "Invalid parameters (required: name and realm)")
		else:
			yield from client.send_message(message.channel, "http://us.battle.net/wow/en/character/{0}/{1}/advanced".format("-".join(params[1:]), params[0])) 

	elif message.content.startswith('!twitch'):
		params = message.content.split(' ')[1:]
		if len(params)<1:
			yield from client.send_message(message.channel, "Invalid parameters (required: name)")
		else:
			yield from client.send_message(message.channel, "http://www.twitch.tv/{0}".format(params[0])) 

	elif message.content.startswith('!whois'):
		params = message.content.split(' ')[1:]
		if ' '.join(params)=="Priestism Bot":
			yield from client.send_message(message.channel, "Hey there, my name is **Priestism Bot**! My other name is **Airi Katagiri**. I'm a 19 year old grill who loves cooking assorted meats. I serve my lord and savior enragednuke-sama.") 
			return
		try:
			fo = open("C:/Users/Dylan/Documents/discord botts/test1/bios/{0}.txt".format(params[0]), "r")
			data = fo.read()
			yield from client.send_message(message.channel, "`{0}`'s data!\n".format(params[0])) 
			yield from client.send_message(message.channel, data)
		except IOError:
			yield from client.send_message(message.channel, "That player does not have a 'Who is?' profile.")
		except IndexError as e:
			yield from client.send_message(message.channel, "Invalid paramaters (error: {0})".format(e))

	elif message.content.startswith("!setwhois"):
		params = message.content.split(' ')[1:]
		user = (message.author.name if len(params)==0 else params[0])
		if message.author.name not in admins() and len(params)>0:
			yield from client.send_message(message.channel, "Only my creator can set other peoples' profiles!")
			user = message.author.name 
		yield from client.send_message(message.channel, "Setting 'Who is?' profile for **{0}**\nPlease type your bio in the next sixty seconds (I recommend copy and pasting a pre-written one!)".format(user))
		resp = yield from client.wait_for_message(timeout=60.0, author=message.author)
		if resp is None:
			yield from client.send_message(message.channel, "Time ran out!") 
		else: 
			fo = open("C:/Users/Dylan/Documents/discord botts/test1/bios/{0}.txt".format(user), "w+")
			fo.write(resp.content)
			yield from client.send_message(message.channel, "Successfully written to {0}'s 'Who is?' profile".format(user)) 

	elif message.content.startswith('+admin'):
		yield from client.send_message(message.channel, "Starting admin addition . . . ") 
		params = message.content.split(' ')[1:]
		name = ' '.join(params)
		if len(params)==0:
			yield from client.send_message(message.channel, "Invalid number of parameters ({0} for 1)".format(len(params))) 
			return
		if name not in admins():
			fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/admins.txt", "a")
			fo.write("|{0}".format(name))
			yield from client.send_message(message.channel, "User {0} successfully added to admin list".format(name))
		else:
			yield from client.send_message(message.channel, "User {0} is already an admin".format(name))

	elif message.content.startswith('-admin'):
		yield from client.send_message(message.channel, "Starting admin removal . . . ") 
		params = message.content.split(' ')[1:]
		name = ' '.join(params)
		if len(params)==0:
			yield from client.send_message(message.channel, "Invalid number of parameters ({0} for 1)".format(len(params))) 
			return
		if name in admins():
			a1 = admins()
			a1.remove(name)
			fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/admins.txt", "w+")
			fo.write('|'.join(a1))
			yield from client.send_message(message.channel, "User {0} successfully removed from admin list".format(name))
		else:
			yield from client.send_message(message.channel, "User {0} is not an admin".format(name))

	elif message.content == "!admins":
		yield from client.send_message(message.channel, "**Current Priestism Bot Admin List**")
		yield from client.send_message(message.channel, '\n'.join(admins()))

	# It is very important you don't let these two (eval and exec) commands be freely used. If someone knows what they're doing,
	# they can mess with your computer fairly easily using these commands
	elif message.content.startswith('!eval'):
		if message.author.name not in admins():
			yield from client.send_message(message.channel, "You are not authorized to use this command")
			return
		try:
			params = ' '.join(message.content.split(' ')[1:])
			yield from client.send_message(message.channel, "Evaluating `{0}`".format(params))
			yield from client.send_message(message.channel, "Result: `{0}`".format(eval(params)))
		except Exception as e:
			yield from client.send_message(message.channel, "An unexpected error occured!\n```\n{0}\n```".format(e))

	elif message.content.startswith('!exec'):
		if message.author.name not in admins():
			yield from client.send_message(message.channel, "You are not authorized to use this command")
			return
		try:
			params = ' '.join(message.content.split(' ')[1:])
			yield from client.send_message(message.channel, "Evaluating `{0}`".format(params))
			yield from client.send_message(message.channel, "Result: `{0}`".format(exec(params)))
		except Exception as e:
			yield from client.send_message(message.channel, "An unexpected error occured!\n```\n{0}\n```".format(e))

	# MMO UPDATE #
	elif message.content.startswith('!mmo'):
		# FILE STRUCTURE #
		# name, class, level, maxhp, maxmana, curhp, curmana, str, int, agi
		params = message.content.split(' ')[1:]
		classes = {0: 'Priest', 1: 'Warrior', 2: 'Wizard', 3: 'Archer', 4: 'Knight'}
		players = [x[:len(x)-4] for x in os.listdir("C:/Users/Dylan/Documents/discord botts/test1/mmo/")]

		if params[0]=='create':
			if len(params)<2:
				yield from client.send_message(message.channel, "Invalid number of parameters ({0} for 2)".format(len(params)))
			elif message.author.name in players:
				yield from client.send_message(message.channel, "You already have a PriestMMO character!")
			else:
				try:
					stats = ""
					yield from client.send_message(message.channel, "**PriestMMO Character Creation**")
					yield from client.send_message(message.channel, "What class would you like to be?\n*Priest* - +1 hp, +1 int, +1 mana\n*Warrior* - +1 hp, +2 str\n*Wizard* - +2 int, +1 mana\n*Archer* - +1 hp, +2 agi\n*Knight* - +2 hp, +1 str")
					response = yield from client.wait_for_message(timeout=15.0, author=message.author)
					if response is None:
						yield from client.send_message(message.channel, "Time has run out, character creation cancelled.")
					elif response.content.lower() == 'priest':
						stats = "06\n2\n6\n2\n1\n2\n1"
					elif response.content.lower() == 'warrior':
						stats = "16\n1\n6\n1\n3\n1\n1"
					elif response.content.lower() == 'wizard':
						stats = "25\n2\n5\n2\n1\n3\n1"
					elif response.content.lower() == 'archer':
						stats = "36\n1\n6\n1\n1\n1\n3"
					elif response.content.lower() == 'knight':
						stats = "46\n1\n6\n1\n2\n1\n1"
					with open("C:/Users/Dylan/Documents/discord botts/test1/mmo/{0}.dat".format(message.author.name), "w+") as f:
						f.write("{0}\n{1}\n1\n{2}".format(' '.join(params[1:]), stats[0], stats[1:])+"\n{}")
					yield from client.send_message(message.channel, "Character {0} has been created!".format(params[1]))
				except Exception as e:
					yield from client.send_message(message.channel, "Something went wrong with character creation. My apologies.\n\nError: {0}".format(e))
		elif params[0]=='stats':
			if len(params)==0:
				yield from client.send_message(message.channel, "Invalid number of parameters ({0} for 1)".format(len(params)))
			name = (message.author.name if len(params)==1 else ' '.join(params[1:]))
			try:
				classes = lambda x: {0: 'Priest', 1: 'Warrior', 2: 'Wizard', 3: 'Archer', 4: 'Knight'}[x]
				data = [(l[:-1] if '\n' in l else l) for l in open("C:/Users/Dylan/Documents/discord botts/test1/mmo/{0}.dat".format(name))]
				print(data)
				yield from client.send_message( message.channel, "Viewing stats for {0}'s character, **{1}**".format(name, data[0]) )
				yield from client.send_message( message.channel, "Level {0} {1}\nHP: {2}/{3}\nMana: {4}/{5}\nStrength: {6}\nIntellect: {7}\nAgility: {8}\nType `!mmo backpack` to view your backpack".format( data[2], classes(int(data[1])), data[3], data[5], data[4], data[6], data[7], data[8], data[9] ) )
			except (FileNotFoundError, IOError):
				yield from client.send_message(message.channel, "That player does not have a PriestMMO character")
			except Exception as e:
				yield from client.send_message(message.channel, "An unknown error occurred when viewing that player's PriestMMO stats\n\nError: {0}".format(e))
		elif params[0]=='backpack':
			with open("C:/Users/Dylan/Documents/discord botts/test1/mmo/{0}.dat".format(message.author.name)) as f:
				player_db = eval(f.readlines()[-1])
				item_db = item_database()
				yield from client.send_message(message.channel, "**{0}**'s Backpack".format(message.author.name))
				for item in player_db:
					yield from client.send_message(message.channel, "{0}x **{1}**".format(player_db[item], item_db[item][0]))
		elif params[0]=='explore':
			stats = pbot_mmo_stats(message.author.name)
			player_level = int(stats[2])
			r = random.randrange(100)+1 #time for some standard game RNGesus
			if r>0 and r<=20:
				yield from client.send_message(message.channel, "(fighting stuff)")
			elif r>20 and r<=30:
				items = item_database()
				print(list(range((player_level-1)*5+1, player_level*5+1)))
				valid_items = [(x, items[x]) for x in items if player_level in range((items[x][1]-1)*5+1, items[x][1]*5+1)]
				i = random.choice(valid_items)
				yield from client.send_message(message.channel, "You found a {0}{1}!".format(i[1][0], "" if message.author.name not in admins() else " (ID: {})".format(i[0])))
				pbot_mmo_update_bags(message.author.name, i[0], 1)
			elif r>30 and r<=97:
				#nothing!
				yield from client.send_message(message.channel, "(nothing of importance happened)")
			elif r==98:
				#+1 str
				yield from client.send_message(message.channel, "(found a tome of ancient blade augment)")
			elif r==99:
				#+1 agi
				yield from client.send_message(message.channel, "(found a tome of ancient archery augment)")
			elif r==100:
				#+1 int
				yield from client.send_message(message.channel, "(found a tome of ancient magicks)")


	# GAMES #
	elif message.content.startswith('!game'):
		params = message.content.split(' ')[1:]
		if len(params)==0:
			yield from client.send_message(message.channel, "Invalid game parameters") 
		elif params[0]=="math":
			if len(params)>4:
				yield from client.send_message(message.channel, "Invalid number of parameters ({0} for 1)".format(len(params)-1))
			else:
				if not params[1].isdigit():
					return 
				if int(params[1]) > 8:
					yield from client.send_message(message.channel, "Please choose a length of 8 or lower")
					return
				op = lambda: {0: '+', 1: '-', 2: '*', 3: '/'}[random.randrange(4)]
				eq = (''.join([op()+str(x) for x in random.sample( range(1, 10 if len(params)<3 else int(params[2]) ), int(params[1]) )]))[1:]
				yield from client.send_message(message.channel, "Equation:\n(Please note that the end result is rounded down, so `1/3*2 = 2`)\n ```\n{0}```".format(eq))
				guess = yield from client.wait_for_message(timeout=(5.0 if len(params)<4 else int(params[3])), author=message.author)
				if guess is None:
					yield from client.send_message(message.channel, "Time has run out! The correct answer was {0}".format(int(eval(eq))))
				elif guess.content == str(int(eval(eq))):
					yield from client.send_message(message.channel, "**Correct!**")
				else:
					yield from client.send_message(message.channel, "**Incorrect!** The correct answer was {0}".format(int(eval(eq))))
		elif params[0]=="guess":
			if len(params)!=2:
				yield from client.send_message(message.channel, "Invalid number of parameters ({0} for 1)".format(len(params)-1))
			else:
				if params[1] == "rules":
					yield from client.send_message(message.channel, "**Rules**\n1. Provide a number for to 0 until it.\n2. You will receive points equal to the number provided if you get it correct.\n3. dont suck")
					return
				elif params[1] == "leaderboard":
					# LEADERBOARD #
					fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/guessgame.txt", "r+")
					data = fo.read()
					dic = eval(data)
					fo.close()
					d_view = [ (v,k) for k,v in dic.items() ]
					d_view.sort(reverse=True)
					to_add = ""
					for v,k in d_view:
						to_add += "{0}: *{1}*\n".format(k,v)
					yield from client.send_message(message.channel, "\n-- **Guess Game Leaderboard** --\n{0}".format(to_add))
					return
					# LEADERBOARD #
				i = int(params[1]) if params[1].isdigit() else 10
				yield from client.send_message(message.channel, "**Guessing game!**\nPlayer: *{0}*\nPlease choose a number between 0 and **{1}**".format(message.author.name, i))
				guess = yield from client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
				answer = random.randrange(i)
				if guess is None:
					yield from client.send_message(message.channel, "Time ran out, the answer was {0}".format(answer))
				elif guess.content == str(answer):
					yield from client.send_message(message.channel, "**Correct!**")
					# LEADERBOARD #
					fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/guessgame.txt", "r+")
					data = fo.read()
					fo.close()
					dic = eval(data)
					if message.author.name in dic:
						dic[message.author.name] = int(dic[message.author.name]) + i
					else:
						dic[message.author.name] = i
					fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/guessgame.txt", "r+")
					fo.truncate()
					fo.write(str(dic))
					fo.close()
					d_view = [ (v,k) for k,v in dic.items() ]
					d_view.sort(reverse=True)
					to_add = ""
					for v,k in d_view:
						to_add += "{0}: *{1}*\n".format(k,v)
					yield from client.send_message(message.channel, "\n-- **Guess Game Leaderboard** --\n{0}".format(to_add))
					# LEADERBOARD #
				else:
					yield from client.send_message(message.channel, "**Incorrect!** The correct answer was {0}".format(answer))

	elif message.content.startswith('+cmd'):
		yield from client.send_message(message.channel, "Command generation starting . . .")
		if message.author.name not in admins():
			yield from client.send_message(message.channel, "You are not authorized for command generation")
			return
		params = message.content.split(' ')[1:]
		try:
			cmd = params[0]
			content = params[1:]
			fo = open("C:/Users/Dylan/Documents/discord botts/test1/cmds/{0}.txt".format(cmd), "w+")
			fo.write(' '.join(content))
			yield from client.send_message(message.channel, "Successfully made command: !{0}".format(cmd))
		except IOError:
			yield from client.send_message(message.channel, "Error finding the file")
		except IndexError:
			yield from client.send_message(message.channel, "Invalid number of parameters ({0} for 2)".format(len(params)))
		except Exception as e:
			yield from client.send_message(message.channel, "An unexpected error occured.\nError: *{0}*".format(e))

	elif message.content.startswith('-cmd'):
		yield from client.send_message(message.channel, "Command removal starting . . .")
		if message.author.name not in admins():
			yield from client.send_message(message.channel, "You are not authorized for command removal")
			return
		params = message.content.split(' ')[1:]
		if len(params)==0 or len(params)>1:
			yield from client.send_message(message.channel, "Invalid parameter count ({0} for 1)".format(len(params)))
			return
		try:
			fo = os.remove("C:/Users/Dylan/Documents/discord botts/test1/cmds/{0}.txt".format(params[0]))
			yield from client.send_message(message.channel, "Successfully removed command: !{0}".format(params[0]))
		except IOError:
			yield from client.send_message(message.channel, "Error generating or reading from file")
		except Exception as e:
			yield from client.send_message(message.channel, "An unexpected error occured.\nError: *{0}*".format(e))

	elif message.content == "!cmds":
		c1 = ["!"+x[:len(x)-4] for x in os.listdir("C:/Users/Dylan/Documents/discord botts/test1/cmds/")]
		yield from client.send_message(message.channel, "**Custom Command List**\n```{0}```".format('\n'.join(c1)))

	elif message.content.startswith('!'):
		command = message.content[1:]
		try:
			fo = open("C:/Users/Dylan/Documents/discord botts/test1/cmds/{0}.txt".format(command), "r")
			data = fo.read()
			output = data.split("[ENDL]")
			for v in output:
				yield from client.send_message(message.channel, v)
		except IOError:
			yield from client.send_message(message.channel, "Invalid command !{0}".format(command))
			yield from client.send_message(message.channel, "BabyRage")



@client.async_event
def on_message_edit(before, after):
	if after.author.name != "Priestism Bot" and after.content != before.content:
		clog("message edit",after.author.name,after.author.id)
		yield from client.send_message(log_server, "Message edited by **{0}** (ID: *{1}*)\n*Previously*: {2} \n*Now*: {3}".format(after.author.name, after.author.id, before.content, after.content))

@client.async_event
def on_message_delete(message):
	if message.author.name != "Priestism Bot":
		clog("message delete",message.author.name,message.author.id)
		yield from client.send_message(log_server, "{0}'s message was deleted".format(message.author.name))

@client.async_event
def on_member_ban(member):
	yield from client.send_message(log_server, "{0} was banned".format(member.name))

@client.async_event
def on_member_unban(server, member):
	yield from client.send_message(log_server, "{0} was unbanned".format(member.name))

@client.async_event
def on_voice_state_update(before, after):
	if before.deaf != after.deaf:
		m = "{0} **IS** {1}".format(before.name, "**NOW** server deafened" if after.deaf else "**NO LONGER** server deafened")
		yield from client.send_message(discord.Object(133761409929576449), m)
	elif before.mute != after.mute:
		m = "{0} **IS** {1}".format(before.name, "**NOW** server muted" if after.mute else "**NO LONGER** server muted")
		yield from client.send_message(discord.Object(133761409929576449), m)
	if before.self_deaf != after.self_deaf:
		m = "{0} **IS** {1}".format(before.name, "**NOW** SELF deafened" if after.self_deaf else "**NO LONGER** SELF deafened")
		yield from client.send_message(discord.Object(133761409929576449), m)
	elif before.self_mute != after.self_mute:
		m = "{0} **IS** {1}".format(before.name, "**NOW** SELF muted" if after.self_mute else "**NO LONGER** SELF muted")
		yield from client.send_message(discord.Object(133761409929576449), m)

def guess_check(m):
	return m.content.isdigit()

def clog(name, user, id):
	print("Command {0} used by {1} (ID: {2})".format(name, user, str(id)))

def pbot_affection(name, value):
	fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/pbot_affection.txt", "r+")
	data = fo.read()
	fo.close()
	dic = eval(data)
	if name in dic:
		dic[name] = dic[name] + value
	else:
		dic[name] = value
	fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/pbot_affection.txt", "r+")
	fo.truncate()
	fo.write(str(dic))
	fo.close()

def get_pbot_affection(name):
	fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/pbot_affection.txt", "r+")
	data = fo.read()
	fo.close()
	dic = eval(data)
	if name in dic.keys():
		return dic[name]
	else:
		return "Who?"

def love_yous(i):
	fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/i-love-yous.txt", "r+")
	data = int(fo.read())
	fo.close()
	fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/i-love-yous.txt", "r+")
	fo.truncate()
	fo.write(str(data+i))
	fo.close()

def get_love_yous():
	fo = open("C:/Users/Dylan/Documents/discord botts/test1/data/i-love-yous.txt", "r+")
	data = int(fo.read())
	fo.close()
	return data

def pbot_mmo_stats(name):
	return [(l[:-1] if ('\n' in l) else l) for l in open("C:/Users/Dylan/Documents/discord botts/test1/mmo/{0}.dat".format(name)).readlines()]

def pbot_mmo_update_bags(name, item_id, amt):
	cur = pbot_mmo_stats(name)
	with open("C:/Users/Dylan/Documents/discord botts/test1/mmo/{0}.dat".format(name), "w+") as f:
		print(cur)
		print(len(cur))
		player_bags = eval(cur[-1])
		if item_id in player_bags:
			player_bags[item_id] += amt
		else:
			player_bags[item_id] = amt
		cur = cur[:-1] + [player_bags]
		f.write('\n'.join([str(x) for x in cur]))

def item_database():
	with open("C:/Users/Dylan/Documents/discord botts/test1/mmo/db/itemDB.db") as f:
		return eval(f.read())

 # # # LOGIN # # #

def get_login():
	fo = open("C:/Users/Dylan/Documents/discord botts/test1/login.txt", "r+")
	return fo.read().split()
client.run(get_login()[0], get_login()[1])

 # # # # # # # # #