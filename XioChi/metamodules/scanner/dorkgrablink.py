#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Module Exploit And Exploit With Metasploit Framework
Created by ~xGans
Facebook : https://web.facebook.com/ichsan.AndroSec
Gmail : Exsandrrt01@gmail.com
you can report bug on my email
'''

import os
import subprocess
from core import wcolors
from core import help
from time import sleep
from core import about
from core import log
options = ["inurl:index.php?id=", "4"]
def dorkgrablink():
	try:
		line_1 = wcolors.color.RED + "[" + wcolors.color.CYAN + "XioChi" + wcolors.color.RED + "]" +  wcolors.color.ENDC
		line_1 += wcolors.color.RED + "[" + wcolors.color.CYAN + "scanner/google_dork" + wcolors.color.RED + "]>> " + wcolors.color.ENDC
		com = raw_input(line_1)
		if com[0:8] =='set dork':
			dork = com[9:9999]
			options[0] = dork
			print wcolors.color.RED + "[" + wcolors.color.CYAN + "Dork" + wcolors.color.RED + "]>> " +wcolors.color.YELLOW+ options[0]
			dorkgrablink()
		elif com[0:8] =='set page':
			pages = com[9:40]
			options[1] = pages
			print wcolors.color.RED + "[" + wcolors.color.CYAN + "Pages" + wcolors.color.RED + "]>> " +wcolors.color.YELLOW+ options[1]
			dorkgrablink()
		elif com[0:12] =='show options':
			print wcolors.color.CYAN+"Options\t\t Value\t\t\t Description"
			print wcolors.color.RED+"---------\t--------------\t\t------------------"
			print wcolors.color.CYAN+"Dork\t\t"+options[0]+"\tInput Dork Value"
			print "Page\t\t"+options[1]+"\t\t\tMax Page Scanning"
			dorkgrablink()
		elif com[0:2] =='os':
			log.logger.single("Command Executed", "\n"+wcolors.color.CYAN)
			os.system(com[3:])
			dorkgrablink()
		elif com[0:4] =='help':
			help.help()
			dorkgrablink()
		elif com[0:4] =='back':
			pass
		elif com[0:5] =='about':
			about.about()
			dorkgrablink()
		elif com[0:3] =='run':
			log.logger.attack("Starting Grab")
			subprocess.Popen('python metamodules/scanner/grab_link.py %s %s' %(options[0], options[1]), shell=True).wait()
			log.logger.attacksukses("Done Grabing")
			dorkgrablink()
		else:
			print wcolors.color.RED + "[" + wcolors.color.CYAN + "Wrong Command" + wcolors.color.RED + "]>> " + com
			dorkgrablink()
	except(KeyboardInterrupt):
		print ""
