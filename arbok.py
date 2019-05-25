#!/usr/bin/python
# coding: utf-8
#ObsiPvP Griefing Tool by zMasonrapa
import socket
import os
import webbrowser
sock = socket.socket()
os.system ("cls")
os.system ("color f0")
opt1 = "Escaner de Puertos"
opt2 = "Escaner de Subdominios"
opt3 = "ForceOP"
opt4 = "Conseguir IP"
opt5 = "Rango de IP"
opt6 = "Lista de Servers"
opt7 = "Nmap tracker"
opt8 = "Ayudante de Comandos"
opt9 = "Cambiar a Ingles"
opt10 = "Salir"
opt11 = "Escaneando... Esto puede llevar un rato..."
opt12 = "Pon la IP Aqui >> "
opt13 = "Escanear Rango Corto"
opt14 = "Escanear Rango Medio"
opt15 = "Escanear Rango Grande"
opt16 = "Setea Tu Opcion"
opt17 = "Musica"

#CONFIGURABLE
#########################################################################################################
authme1 = input ("Please, set your ""Username : """)
if authme1 == "masonrapa":   #DELETE THE DEFAULT USER FOR NO LOGIN 
	passmasonrapa = input ("Please, set your ""Password : """)
	if passmasonrapa == "12345": #DELETE THE DEFAUL PASSWORD FOR NO LOGIN
#########################################################################################################

		while True:
			input()
			os.system ("cls")
			print("´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
			print(" ´´´´´´´´´´´´´´´´´´__________´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
			print(" ´´´´´´´´´´´´´´´´´""/|___""______|""´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
			print(" ´´´´´´´´´´´´´´´´""|. . .___""___|================0´´´´´´´´´´D´´´´´D´´´´D´´´´D´´´")
			print(" ´´´´´´´´´´´´´´´ ""|______""_____|""´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
			print(" ´´´´´´´´=========/. . . . . . =========_´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
			print(" ´´´´´ /  B Y : Z M A"" S O N R A P A . . .|´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
			print(" ´´´´´/´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´|´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
			print(" ´´´´´|´ O O O O O O O O O O O O O O O O O´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´")
			print ()
			print ("***""**********************************""           O")
			print ("***  Hello "+(authme1)+"              ***           B")
			print ("***""  Setea tu opcion              ""***""           S")
			print ("***""**********************************""           I")
			print ("***"+"  1) "+(opt1)+"        ""***")
			print ("***"+"  2) "+(opt2)+"    ""***""           T")
			print ("***"+"  3) "+(opt3)+"                   ""***""           O")
			print ("***"+"  4) "+(opt4)+"              ""***""           O")
			print ("***"+"  5) "+(opt5)+"               ""***""           L")
			print ("***"+"  6) "+(opt6)+"          ""***")
			print ("***"+"  7) "+(opt7)+"              ""***")
			print ("***"+"  8) "+(opt8)+"      ""***")
			print ("***"+"  9) "+(opt9)+"          ""***")
			print ("***"+"  10) "+(opt17)+"                   ""***")
			print ("***"+"  11) "+(opt10)+"                    ""***")
			print ("***""**********************************")
			x = input (""+(opt16)+" [1/11] >> """)
			if x == "11":
				exit()
			elif x == "1":
				ipvic = input (""+opt12+"")
				print ("1) "+opt13+" '1-80' ")
				print ("2) "+opt14+" '25500-25600' ")
				print ("3) "+opt15+" '65500-65535' ")
				ranz = input ("Selecciona tu opcion de escaneo >> """)
				if ranz == "1":
					rka = range(1,80)        #CONFIGURABLE
				elif ranz == "2":
					rka = range(25500,25600) #CONFIGURABLE
				elif ranz == "3":
					rka = range(65530,65535) #CONFIGURABLE
				print (opt11)
				for puertos in (rka):
					try:
						socka = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						resultadofinal = socka.connect_ex((ipvic, puertos))
						if resultadofinal == 0:
							print (str(ipvic)+":"+str(puertos))
						socka.close()
					except:
						pass
			elif x == "3":
				subdomains = ["build", "play"]
				victima = input (opt12)
				print (opt11)
				for ejecutar in subdomains:
					try:
						hosts = str(ejecutar) + "." + str(victima)
						iphost = socket.gethostbyname(str(hosts))
						try:
							for port in range(25560,25575):
								sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								result = sock.connect_ex((iphost, port))
								if result == 0:
									print (str(iphost)+":"+str(port))
								sock.close()
						except:
							pass
					except:
						pass
			elif x == "2":
				os.system ("cls")     #CONFIGURABLE
				subdomains0 = ["www", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets"]
				victima0 = input (opt12)
				for ejecutar0 in subdomains0:
					try:
						ipserver0 = str(ejecutar0)+"."+str(victima0)
						iphost0 = socket.gethostbyname(str(ipserver0))
						print ("[ObsiTool] (Subdomain) >> """+str(ejecutar0)+"."+str(victima0)+" >> """+str(iphost0))
					except:
						pass
			elif x == "4":
				os.system ("cls")
				asd = input (opt12)
				dsa = socket.gethostbyname(str(asd))
				print ((dsa))
			elif x == "7":
				os.system ("cls")
				print (opt12)
				a = input ("Set your first IP [1/4] (127) >> ")
				b = input ("Set your first IP [2/4] (0) >> ")
				c = input ("Set your first IP [3/4] (0) >> ")
				x = input ("Set your first IP [4/4] (1) >> ")
				y = int(1)
				z = int(x) - int(y)
				r = int(x) + int(y)
				ipresul = str(a)+"."+str(b)+"."+str(c)+"."+str(z)+"-"+str(r)
				print ("")
				os.system ("nmap -p 1-12,1000-1010,20000-20005,25500-25600,28010-28015,30000-30005,40000-40010,65500-65535 -T5 -v -A -Pn "+ipresul)
			elif x == "5":
				from socket import *
				open_ports = []
				stty = input (opt12)
				print (""+opt11)
				for la in range(0, 255):
					try:
						rangeIP = stty+str(la)
						socky = socket(AF_INET, SOCK_STREAM)
						resulta3 = socky.connect_ex((rangeIP, 25565))
						if resulta3 == 0:
							open_ports.append(str(rangeIP)+":25565")
						socky.close()
					except KeyboardInterrupt:
						pass
				for resulta4 in open_ports:
					print ((resulta4))
			elif x == "9":    #CONFIGURABLE
				opt1 = "Port Scanner      "
				opt2 = "Subdomain Scanner     "
				opt3 = "ForceOP"
				opt4 = "Get IP      "
				opt5 = "IP Range   "
				opt6 = "Server List     "
				opt7 = "Nmap tracker"
				opt8 = "Command Helper      "
				opt9 = " LOCKED OPTION  "
				opt10 = "Exit "
				opt11 = "Scaning... This may take a while..."
				opt12 = "Put Your IP Here >> "
				opt13 = "Scan Short Range"
				opt14 = "Scan Medium Range"
				opt15 = "Scan Long Range"
				opt16 = "Set Your Option"
				opt17 = "Music "
				
			elif x == "6":
				from random import seed
				from random import randint
				for _ in range(1):
					value = randint(1, 150)
				if value == 1:
					print ("hub.mcs.gg")
				if value == 2:
					print ("play.becto.net")
				if value == 3:
					print ("PLAY.ROYALLEGACY.NET")
				if value == 4:
					print ("pvp.desteria.com")
				if value == 5:
					print ("play.manacube.net")
				if value == 6:
					print ("play.extremecraft.net")
				if value == 7:
					print ("mc-central.net")
				if value == 8:
					print ("pixel.mc-complex.com")
				if value == 9:
					print ("mineheroes.net")
				if value == 10:
					print ("mc.snapcraft.net")
				if value == 11:
					print ("MC.Performium.net")
				if value == 12:
					print ("play.applecraft.org")
				if value == 13:
					print ("play.jartexnetwork.com")
				if value == 14:
					print ("play.thedestinymc.com")
				if value == 15:
					print ("play.vexedmc.com")
				if value == 16:
					print ("earthmc.net")
				if value == 17:
					print ("play.pixelmonrealms.com")
				if value == 18:
					print ("mc-gtm.net")
				if value == 19:
					print ("FadeCloud.com")
				if value == 20:
					print ("FadeCloud.com")
				if value == 21:
					print ("pvp.desteria.com")
				if value == 22:
					print ("pixel.rc-gamers.com")
				if value == 23:
					print ("eu.sonoyuncu.network")
				if value == 24:
					print ("PlayPokeNinjas.com")
				if value == 25:
					print ("DIRTCRAFT.GG")
				if value == 26:
					print ("jogar.gearfriends.net")
				if value == 27:
					print ("play.strongcraft.org")
				if value == 28:
					print ("play.pika-network.net")
				if value == 29:
					print ("mc.ecuacraft.com")
				if value == 30:
					print ("play.ggmc.me")
				if value == 31:
					print ("play.castiamc.com")
				if value == 32:
					print ("play.projectwonder.net")
				if value == 33:
					print ("play.mineville.org")
				if value == 34:
					print ("pixel.mc-blaze.com")
				if value == 35:
					print ("play.MuxMC.net")
				if value == 36:
					print ("jogar.rocketmc.com.br")
				if value == 37:
					print ("play.omegacraft.cl")
				if value == 38:
					print ("oyna.provanas.com")
				if value == 39:
					print ("play.uniocraft.com")
				if value == 40:
					print ("mineverse.com")
				if value == 41:
					print ("mc.minebox.es")
				if value == 42:
					print ("mc.ventureland.net")
				if value == 43:
					print ("Pokecentral.org")
				if value == 44:
					print ("play.azertumc.com")
				if value == 45:
					print ("mc.momentonetwork.net")
				if value == 46:
					print ("play.wildercraft.net")
				if value == 47:
					print ("play.mc-complex.com")
				if value == 48:
					print ("Play.Betacraft.Org")
				if value == 49:
					print ("play.wheelcraft-id.net")
				if value == 50:
					print ("smp.hometownmc.com")
				if value == 51:
					print ("mc.safesurvival.net")
				if value == 52:
					print ("play.cultivatemc.com")
				if value == 53:
					print ("play.alttd.com")
				if value == 54:
					print ("play.limitlessmc.net")
				if value == 55:
					print ("mc.clubobsidian.com")
				if value == 56:
					print ("play.pokeverse.org")
				if value == 57:
					print ("play.bulbacraft.com")
				if value == 58:
					print ("Play.Minecraft-Romania.Ro")
				if value == 59:
					print ("fun.multyplay.ro")
				if value == 60:
					print ("miningdead.com")
				if value == 61:
					print ("play.primemc.org")
				if value == 62:
					print ("jogar.luthcraft.com")
				if value == 63:
					print ("minelife.dk")
				if value == 64:
					print ("play.pokemayhem.com")
				if value == 65:
					print ("play.skyblocknetwork.com")
				if value == 66:
					print ("mc.PokeSmash.co")
				if value == 67:
					print ("play.ajgaming.net")
				if value == 68:
					print ("play.guildcraft.org")
				if value == 69:
					print ("mc.soulplex.net")
				if value == 70:
					print ("play.mineway.org")
				if value == 71:
					print ("mc.playdreamcraft.com.br")
				if value == 72:
					print ("mc.myftb.de")
				if value == 73:
					print ("mc.akarcraft.es")
				if value == 74:
					print ("jogar.pokelandia.com")
				if value == 75:
					print ("arefy.net")
				if value == 76:
					print ("mcm.datblock.com")
				if value == 77:
					print ("play.apeironmc.com")
				if value == 78:
					print ("mc.kingnw.com")
				if value == 79:
					print ("play.battleasya.com")
				if value == 80:
					print ("play.onlymc.net")
				if value == 81:
					print ("servicraft.org")
				if value == 82:
					print ("DBC.ApolloNetworkMC.net")
				if value == 83:
					print ("play.primemc.org")
				if value == 84:
					print ("mc.megaplanet.net")
				if value == 85:
					print ("play.skyblocknetwork.com")
				if value == 86:
					print ("mc.PokeSmash.co")
				if value == 87:
					print ("mc.akarcraft.es")
				if value == 88:
					print ("play.PrismForge.com")
				if value == 89:
					print ("mc.survival.pw")
				if value == 90:
					print ("play.potterworldmc.com")
				if value == 91:
					print ("play.journeygaming.com")
				if value == 92:
					print ("pixel.un-linked.com")
				if value == 93:
					print ("mc.kriptonpvp.com")
				if value == 94:
					print ("play.peacefulfarms.net")
				if value == 95:
					print ("tekkit.mc-complex.com")
				if value == 96:
					print ("mcmp.AspiriaMc.com")
				if value == 97:
					print ("play.breachpvp.com")
				if value == 98:
					print ("Pixelmon.HappyCloudMC.com")
				if value == 99:
					print ("play.minewonderland.net")
				if value == 100:
					print ("my.mineland.net")
				if value == 101:
					print ("mc.kgb-minecraft.info")
				if value == 102:
					print ("play.pokedash.org")
				if value == 103:
					print ("Play.DipCraft.Ro")
				if value == 151:
					print ("play.breakdowncraft.com")
				if value == 104:
					print ("play.pixelmonadventures.com")
				if value == 105:
					print ("play.mineswift.net")
				if value == 105:
					print ("omegarealm.com")
				if value == 106:
					print ("play.skybattle.net")
				if value == 106:
					print ("mc.ultranetwork.me")
				if value == 107:
					print ("jogar.craftsgp.net")
				if value == 108:
					print ("geoblock.es")
				if value == 109:
					print ("play.pixelmonharmony.com")
				if value == 110:
					print ("play.xenolithnetwork.com")
				if value == 111:
					print ("play.conspiracycraft.net")
				if value == 112:
					print ("play.creativefun.net")
				if value == 113:
					print ("play.phanaticmc.com")
				if value == 114:
					print ("tinetwork.net")
				if value == 115:
					print ("play.decimatepvp.com")
				if value == 116:
					print ("play.YomNetwork.ca")
				if value == 117:
					print ("play.silkycraft.net")
				if value == 118:
					print ("play.nytro.network")
				if value == 119:
					print ("mc.aminearserver.es")
				if value == 120:
					print ("play.lunarrisingmc.com")
				if value == 121:
					print ("InfinityCubedMC.com")
				if value == 122:
					print ("play.minelink.net")
				if value == 123:
					print ("SB-Central.com")
				if value == 124:
					print ("play.voidrealms.net")
				if value == 125:
					print ("play.ickcraft.nl")
				if value == 126:
					print ("play.hallowedfantasy.com")
				if value == 127:
					print ("mc.lotc.co")
				if value == 128:
					print ("play.poke-brawl.com")
				if value == 129:
					print ("play.feroxmc.net")
				if value == 130:
					print ("mc.pvpbulgaria.eu")
				if value == 131:
					print ("jogar.backmc.com.br")
				if value == 132:
					print ("play-pokecraft.com")
				if value == 133:
					print ("play.eminentmc.com")
				if value == 134:
					print ("play.dawnhaven.net")
				if value == 135:
					print ("massivecraft.com")
				if value == 136:
					print ("mc.divictusgaming.com")
				if value == 137:
					print ("play.acornmc.org")
				if value == 138:
					print ("vnlla.net")
				if value == 139:
					print ("play.shadownode.ca")
				if value == 140:
					print ("mc.calderaminecraft.com")
				if value == 141:
					print ("play.ghiblicraft.com")
				if value == 142:
					print ("diamond.voxmc.com")
				if value == 143:
					print ("server.proyecto40.es")
				if value == 144:
					print ("play.cursedcraft.com")
				if value == 145:
					print ("play.harvestmc.net")
				if value == 146:
					print ("play.harvestmc.net")
				if value == 147:
					print ("DangCap.Ga")
				if value == 148:
					print ("twerion.net")
				if value == 149:
					print ("play.poke-saga.com")
				if value == 150:
					print ("mc.feargames.it")
			elif x == "8":
				os.system ("cls")
				print (" 1) Spamm Commands ")
				print (" 2) Destruction Commands ")
				print (" 3) Troll Commands ")
				print (" 4) AutoOP Commands ")
				print (" 5) Permission PL  ")
				pregun = input ("Setea tu opcion >> "+"")
				os.system ("cls")
				if pregun == "1":
					esset = input ("El Server tiene essentials??? [YES/NO] >>>> "+"")
					if esset == "NO":
						execut3 = "/minecraft:say"
					elif esset == "YES":
						execut3 = "/ept ebc"
					else:
						print ("error :/")
					essen1 = input ("Is a Spanish Server??? [YES/NO] >>> "+"")
					if essen1 == "YES":
						print ("1) YT/TG Channel Spam ")
						print ("2) User /// Squad Spam")
						print ("3) User + Squad + YT/TG")
						prag = input ("Setea tu Opcion >> "+"")
						os.system ("cls")
						if prag == "1":
							ytchan = input ("Pon la URL >>>  "+"")
							os.system ("cls")
							print ((execut3)+" &5El Server Esta Siendo &4&lHACKEADO &6por "+(ytchan)+" &2Suscribanse para tener &aOP!!")
						if prag == "2":
							user1 = input ("Pon tu Username >>>  "+"")
							os.system ("cls")
							print ((execut3)+" &4&kasdf &dServidor &6Grifeado &bPor: &9&l"+(user1))
						if prag == "3":
							chan2 = input ("Pon tu YT Channel >>>  ")
							sqad2 = input ("Pon tu Squad Name >>>  ")
							os.system ("cls")
							print ((execut3)+" &aServer Atacado por &4"+(sqad2)+" &6Suscribete a &2"+(chan2))
					
					if essen1 == "NO":
						print ("1) YT/TG Channel Spam ")
						print ("2) User /// Squad Spam")
						print ("3) User + Squad + YT/TG")
						prag = input ("Put Your Option >> "+"")
						os.system ("cls")
						if prag == "1":
							ytchan = input ("Put The URL >>> "+"")
							os.system ("cls")
							print ((execut3)+" &5The Server have been by &4&lHACKED "+(ytchan)+" &2Suscribe for get &aOP!!")
						if prag == "2":
							user1 = input ("Put The Username >>> "+"")
							os.system ("cls")
							print ((execut3)+" &4&kasdf &dServer &6Griefed &bBy: &9&l"+(user1))
						if prag == "3":
							chan2 = input ("Put The YT Channel >>> "+"")
							sqad2 = input ("Put The Squad Name >>>  "+"")
							os.system ("cls")
							print ((execut3)+" &aThe Server have been attacked &4"+(sqad2)+" &Suscribe to &2"+(chan2))
					
				elif pregun == "2":
					pregwe = input ("Have The Server World Edit Plugin??? [YES/NO] >>>  "+"")
					if pregwe == "YES":
						preges = input ("Have The Server Essentials Plugin??? [YES/NO] >>> "+"")
						if preges == "YES":
							os.system ("cls")
							print ("/ept /sphere 0 10")
							print ("/ept /cyl lava 5")
						if preges == "NO":
							os.system ("cls")
							print ("/br sphere 0 5")
							print ("/sp area 5")
					if pregwe == "NO":
						os.system ("cls")
						print ("/fill ~-10 ~-2 ~-10 ~10 ~2 ~10 air")
						print ("/fill ~-5 ~-5 ~-5 ~5 ~5 ~5 lava")
						print ("/minecraft:summon PrimedTnt")
						
				elif pregun == "3":
					os.system ("cls")
					print ("/effect 1 255 255")
					print ("/minecraft:tp @a @p")
					print ("/fill ~0 ~30 ~0 ~0 ~30 ~0 anvil")
					
				elif pregun == "4":
					pregop = input ("Have The Server Essentials Plugin??? [YES/NO] >>> "+"")
					if pregop == "YES":
						os.system ("cls")
						print ("/epowertool minecraft:op [USER]")
					if pregop == "NO":
						os.system ("cls")
						print ("/minecraft:execute 0 0 0 @p minecraft:op @p")

				elif pregun == "5":
					os.system ("cls")
					usrknow = input ("Set Your Nickname >>>  "+"")
					os.system ("cls")
					print ("1) PermissionEx ")
					print ("2) LuckyPerms ")
					print ("3) PowerFulPerms ")
					print ("4) UltraPermissions ")
					print ("5) GroupManager ")
					print ("6) zPermissions  ")
					print ("7) No Plugins ")
					print ()
					pregperms = input ("Set Your Option [1-7] >>>  "+"")
					if pregperms == "1":
						os.system ("cls")
						print ("/pex user "+(usrknow)+" add *")
					elif pregperms == "2":
						os.system ("cls")
						print ("/lp user "+(usrknow)+" set *")
					elif pregperms == "3":
						os.system ("cls")
						print ("/pp "+(usrknow)+" add *")
					elif pregperms == "4":
						os.system ("cls")
						print ("/ups addpermission "+(usrknow)+" *")
					elif pregperms == "5":
						os.system ("cls")
						print ("/manuaddp "+(usrknow)+" *")
					elif pregperms == "6":
						os.system ("cls")
						print ("/permissions player "+(usrknow)+" set *")
					elif pregperms == "7":
						os.system ("cls")
						print ("/minecraft:op "+(usrknow))
					else:
						os.system ("cls")
						print ("No valid Option")
			elif x == "10":
				os.system ("cls")
				print ("Dont you know what song put in your griefing videos??? : O ")
				print ()
				print ()
				print ("Select a music type")
				print ("1) SPANISH TRAP")
				print ("2) ENGLISH TRAP")
				print ("3) ELECTRO")
				print ("4) NIGHTCORE")
				print ()
				musqu = input ("Select Your Type [1-4] >>> "+"")
				if musqu == "1":
					from random import seed
					from random import randint
					for _ in range(1):
						value1 = randint(1, 20)
					if value1 == 1:
						webbrowser.open("https://www.youtube.com/watch?v=OSUxrSe5GbI", new=2, autoraise=True)
					elif value1 == 2:
						webbrowser.open("https://www.youtube.com/watch?v=9jI-z9QN6g8", new=2, autoraise=True)
					elif value1 == 3:
						webbrowser.open("https://www.youtube.com/watch?v=BvFJstCIrpw", new=2, autoraise=True)
					elif value1 == 4:
						webbrowser.open("https://www.youtube.com/watch?v=bg64AFnRnkc", new=2, autoraise=True)
					elif value1 == 5:
						webbrowser.open("https://www.youtube.com/watch?v=bcHTl9h7TWI", new=2, autoraise=True)
					elif value1 == 6:
						webbrowser.open("https://www.youtube.com/watch?v=kMPW3AvBf_o", new=2, autoraise=True)
					elif value1 == 7:
						webbrowser.open("https://www.youtube.com/watch?v=3SHJ5OywydA", new=2, autoraise=True)
					elif value1 == 8:
						webbrowser.open("https://www.youtube.com/watch?v=Hzhvpr9mZQ8", new=2, autoraise=True)
					elif value1 == 9:
						webbrowser.open("https://www.youtube.com/watch?v=LChVJL08dus", new=2, autoraise=True)
					elif value1 == 10:
						webbrowser.open("https://www.youtube.com/watch?v=A_fCv76c4uQ", new=2, autoraise=True)
					elif value1 == 11:
						webbrowser.open("https://www.youtube.com/watch?v=XrLzZdBGTAk", new=2, autoraise=True)
					elif value1 == 12:
						webbrowser.open("https://www.youtube.com/watch?v=n58WaCa9Cl0", new=2, autoraise=True)
					elif value1 == 13:
						webbrowser.open("https://www.youtube.com/watch?v=Q4Js9OEODHM", new=2, autoraise=True)
					elif value1 == 14:
						webbrowser.open("https://www.youtube.com/watch?v=d0oLWETQS4s", new=2, autoraise=True)
					elif value1 == 15:
						webbrowser.open("https://www.youtube.com/watch?v=T-24_QGaYSE", new=2, autoraise=True)
					elif value1 == 16:
						webbrowser.open("https://www.youtube.com/watch?v=0m3pGVWWRgw", new=2, autoraise=True)
					elif value1 == 17:
						webbrowser.open("https://www.youtube.com/watch?v=IveTpXasFDg", new=2, autoraise=True)
					elif value1 == 18:
						webbrowser.open("https://www.youtube.com/watch?v=uc_EUssELy4", new=2, autoraise=True)
					elif value1 == 19:
						webbrowser.open("https://www.youtube.com/watch?v=CWCxuDnVVkU", new=2, autoraise=True)
					elif value1 == 20:
						webbrowser.open("https://www.youtube.com/watch?v=4o64oHEZWkU", new=2, autoraise=True)
						
				elif musqu == "2":
					from random import seed
					from random import randint
					for _ in range(1):
						value2 = randint(1, 20)
					if value2 == 1:
						webbrowser.open("https://www.youtube.com/watch?v=OC7cNS0GINo", new=2, autoraise=True)
					elif value2 == 2:
						webbrowser.open("https://www.youtube.com/watch?v=BqVe_agO9IE", new=2, autoraise=True)
					elif value2 == 3:
						webbrowser.open("https://www.youtube.com/watch?v=31j4DIpgY9U", new=2, autoraise=True)
					elif value2 == 4:
						webbrowser.open("https://www.youtube.com/watch?v=pgN-vvVVxMA", new=2, autoraise=True)
					elif value2 == 5:
						webbrowser.open("https://www.youtube.com/watch?v=FAucVNRx_mU", new=2, autoraise=True)
					elif value2 == 6:
						webbrowser.open("https://www.youtube.com/watch?v=7JGDWKJfgxQ", new=2, autoraise=True)
					elif value2 == 7:
						webbrowser.open("https://www.youtube.com/watch?v=Gnxvy8TitSs", new=2, autoraise=True)
					elif value2 == 8:
						webbrowser.open("https://www.youtube.com/watch?v=UceaB4D0jpo", new=2, autoraise=True)
					elif value2 == 9:
						webbrowser.open("https://www.youtube.com/watch?v=SC4xMk98Pdc", new=2, autoraise=True)
					elif value2 == 10:
						webbrowser.open("https://www.youtube.com/watch?v=cwQgjq0mCdE", new=2, autoraise=True)
					elif value2 == 11:
						webbrowser.open("https://www.youtube.com/watch?v=V_MXGdSBbAI", new=2, autoraise=True)
					elif value2 == 12:
						webbrowser.open("https://www.youtube.com/watch?v=GX8Hg6kWQYI", new=2, autoraise=True)
					elif value2 == 13:
						webbrowser.open("https://www.youtube.com/watch?v=VWoIpDVkOH0", new=2, autoraise=True)
					elif value2 == 14:
						webbrowser.open("https://www.youtube.com/watch?v=gAs9HZC9c7Y", new=2, autoraise=True)
					elif value2 == 15:
						webbrowser.open("https://www.youtube.com/watch?v=xTlNMmZKwpA", new=2, autoraise=True)
					elif value2 == 16:
						webbrowser.open("https://www.youtube.com/watch?v=lwk5OUII9Vc", new=2, autoraise=True)
					elif value2 == 17:
						webbrowser.open("https://www.youtube.com/watch?v=Hn7WDtF3nKA", new=2, autoraise=True)
					elif value2 == 18:
						webbrowser.open("https://www.youtube.com/watch?v=DmWWqogr_r8", new=2, autoraise=True)
					elif value2 == 19:
						webbrowser.open("https://www.youtube.com/watch?v=2FsnVCLYcrM", new=2, autoraise=True)
					elif value2 == 20:
						webbrowser.open("https://www.youtube.com/watch?v=DPxL7dO5XPc", new=2, autoraise=True)
						
				elif musqu == "3":
					from random import seed
					from random import randint
					for _ in range(1):
						value3 = randint(1, 20)
					if value3 == 1:
						webbrowser.open("https://www.youtube.com/watch?v=8xlDwukxjnA", new=2, autoraise=True)
					elif value3 == 2:
						webbrowser.open("https://www.youtube.com/watch?v=8Tu0lcl75yg", new=2, autoraise=True)
					elif value3 == 3:
						webbrowser.open("https://www.youtube.com/watch?v=QglaLzo_aPk", new=2, autoraise=True)
					elif value3 == 4:
						webbrowser.open("https://www.youtube.com/watch?v=ih2xubMaZWI", new=2, autoraise=True)
					elif value3 == 5:
						webbrowser.open("https://www.youtube.com/watch?v=Los42buIecE", new=2, autoraise=True)
					elif value3 == 6:
						webbrowser.open("https://www.youtube.com/watch?v=qn-X5A0gbMA", new=2, autoraise=True)
					elif value3 == 7:
						webbrowser.open("https://www.youtube.com/watch?v=jK2aIUmmdP4", new=2, autoraise=True)
					elif value3 == 8:
						webbrowser.open("https://www.youtube.com/watch?v=K4DyBUG242c", new=2, autoraise=True)
					elif value3 == 9:
						webbrowser.open("https://www.youtube.com/watch?v=euCqAq6BRa4", new=2, autoraise=True)
					elif value3 == 10:
						webbrowser.open("https://www.youtube.com/watch?v=12CeaxLiMgE", new=2, autoraise=True)
					elif value3 == 11:
						webbrowser.open("https://www.youtube.com/watch?v=w-8lw7vDHQU", new=2, autoraise=True)
					elif value3 == 12:
						webbrowser.open("https://www.youtube.com/watch?v=EU5HpiJJasU", new=2, autoraise=True)
					elif value3 == 13:
						webbrowser.open("https://www.youtube.com/watch?v=cvq7Jy-TFAU", new=2, autoraise=True)
					elif value3 == 14:
						webbrowser.open("https://www.youtube.com/watch?v=Gqm0_fvkYZI", new=2, autoraise=True)
					elif value3 == 15:
						webbrowser.open("https://www.youtube.com/watch?v=NbfOZ6ehf6o", new=2, autoraise=True)
					elif value3 == 16:
						webbrowser.open("https://www.youtube.com/watch?v=Rpr_HNJ0Y3A", new=2, autoraise=True)
					elif value3 == 17:
						webbrowser.open("https://www.youtube.com/watch?v=9vMh9f41pqE", new=2, autoraise=True)
					elif value3 == 18:
						webbrowser.open("https://www.youtube.com/watch?v=oC-GflRB0y4", new=2, autoraise=True)
					elif value3 == 19:
						webbrowser.open("https://www.youtube.com/watch?v=exJlapzPnlc", new=2, autoraise=True)
					elif value3 == 20:
						webbrowser.open("https://www.youtube.com/watch?v=1EuXN9zXnYQ", new=2, autoraise=True)
						
				elif musqu == "4":
					from random import seed
					from random import randint
					for _ in range(1):
						value4 = randint(1, 20)
					if value4 == 1:
						webbrowser.open("https://www.youtube.com/watch?v=3caAitEusSw", new=2, autoraise=True)
					elif value4 == 2:
						webbrowser.open("https://www.youtube.com/watch?v=Vxr87jAn_eo", new=2, autoraise=True)
					elif value4 == 3:
						webbrowser.open("https://www.youtube.com/watch?v=nRrkeUJxJRE", new=2, autoraise=True)
					elif value4 == 4:
						webbrowser.open("https://www.youtube.com/watch?v=8N_aay0ddcY", new=2, autoraise=True)
					elif value4 == 5:
						webbrowser.open("https://www.youtube.com/watch?v=EGLmKeQzYlo", new=2, autoraise=True)
					elif value4 == 6:
						webbrowser.open("https://www.youtube.com/watch?v=fFUVHyM_vYU", new=2, autoraise=True)
					elif value4 == 7:
						webbrowser.open("https://www.youtube.com/watch?v=blBDU7G0_Oo", new=2, autoraise=True)
					elif value4 == 8:
						webbrowser.open("https://www.youtube.com/watch?v=cvaIgq5j2Q8", new=2, autoraise=True)
					elif value4 == 9:
						webbrowser.open("https://www.youtube.com/watch?v=bOpLs6qfYoI", new=2, autoraise=True)
					elif value4 == 10:
						webbrowser.open("https://www.youtube.com/watch?v=c0mX-5q3mrY", new=2, autoraise=True)
					elif value4 == 11:
						webbrowser.open("https://www.youtube.com/watch?v=cyW2ajAVyfA", new=2, autoraise=True)
					elif value4 == 12:
						webbrowser.open("https://www.youtube.com/watch?v=tOoVFIr-Eas", new=2, autoraise=True)
					elif value4 == 13:
						webbrowser.open("https://www.youtube.com/watch?v=RKhAmgOopfc", new=2, autoraise=True)
					elif value4 == 14:
						webbrowser.open("https://www.youtube.com/watch?v=phK-ddhP6MY", new=2, autoraise=True)
					elif value4 == 15:
						webbrowser.open("https://www.youtube.com/watch?v=gpJMrrkfLZU", new=2, autoraise=True)
					elif value4 == 16:
						webbrowser.open("https://www.youtube.com/watch?v=FBuPQcv0uTc", new=2, autoraise=True)
					elif value4 == 17:
						webbrowser.open("https://www.youtube.com/watch?v=ckphmp0hzGM", new=2, autoraise=True)
					elif value4 == 18:
						webbrowser.open("https://www.youtube.com/watch?v=98BLIuxJHWA", new=2, autoraise=True)
					elif value4 == 19:
						webbrowser.open("https://www.youtube.com/watch?v=HZYihvoBBGw", new=2, autoraise=True)
					elif value4 == 20:
						webbrowser.open("https://www.youtube.com/watch?v=HyxUSqcYpLE", new=2, autoraise=True)
			
else:
	exit()
