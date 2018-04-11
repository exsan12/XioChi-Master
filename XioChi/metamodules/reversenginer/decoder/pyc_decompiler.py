# -*- coding: utf-8 -*-

'''
Pyc Executable Decompiler
Coded By ./Xi4u7
AndroSec1337 Cyber Team
https://facebook.com/Xi4u7
'''
import uncompyle6


# -*- coding: utf-8 -*-

'''
Wordress Download Manager Exploit
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
from core import about
import requests
options = ["/path/to/script.pyc","/path/to/output.py"]

def pyc_deco():
	try:
		line_1 = color.RED + "[" + color.CYAN + "XioChi" + color.RED + "]" +  color.ENDC
		line_1 += color.RED + "[" + color.CYAN + "reversenginer/pyc_decompiler" + color.RED + "]>> " + color.ENDC
		com = raw_input(line_1)
		com = com.lower()
		if com[0:9] =='set input':
			input = com[10:40]
			options[0] = input
			print color.RED + "[" + color.CYAN + "Target" + color.RED + "]>> " + options[0]
			pyc_deco()
		if com[0:10] =='set output':
			output = com[11:40]
			options[1] = output
			print color.RED + "[" + color.CYAN + "Target" + color.RED + "]>> " + options[1]
			pyc_deco()
		elif com[0:12] =='show options':
			print ""
			print "Options\t\t Value\t\t\tRQ\t Description"
			print "---------\t--------------\t\t----\t--------------"
			print "INPUT\t\t"+options[0]+"\tyes\tSource Encoded"
			print "OUTPUT\t\t"+options[1]+"\tyes\tOutput To Decoded"
			pyc_deco()
		elif com[0:2] =='os':
			log.logger.single("Command Executed", "\n"+color.CYAN)
			os.system(com[3:])
			pyc_deco()
		elif com[0:4] =='help':
			help.help()
			pyc_deco()
		elif com[0:4] =='back':
			pass
		elif com[0:5] =='about':
			about.about()
			pyc_deco()
		elif com[0:3] =='run':
			log.logger.attack('Reverse Enginer - Pyc Decompiler')
			script = options[0]
			output = options[1]
			try:
				from time import sleep
				with open(output, "wb") as out:
					sleep(3)
					log.logger.attack('Decompile Resources...')
					uncompyle6.uncompyle_file(script, out)
					sleep(2)
					log.logger.attack('Proccess Decompile Done...')
					pyc_deco()
			except Exception as e:
				log.logger.error(str(e))
				pyc_deco()
		else:
			print color.RED + "[" + color.CYAN + "Wrong Command" + color.RED + "]>>" + com
			pyc_deco()
	except(KeyboardInterrupt):
		print ""
