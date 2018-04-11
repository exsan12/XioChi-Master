#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Module for Remote Desktop Exploit With Metasploit Framework
Created by ~xGans
Facebook : https://web.facebook.com/ichsan.AndroSec
Gmail : Exsandrrt01@gmail.com
you can report bug on my email
'''
import sys
import time
RESET = "\033[0m"
PURPLE = '\033[95m'
CYAN = '\033[37;1m' # '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[37;1m' # '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[31;1m' # '\033[91m'
BOLD = '\033[1m'
UNDERL = '\033[4m'
ENDC = '\033[0m'
backBlack = '\033[40m'
backRed = '\033[41m'
backGreen = '\033[42m'
backYellow = '\033[43m'
backBlue = '\033[44m'
backMagenta = '\033[45m'
backCyan = '\033[46m'
backWhite = '\033[47m'
class logger(object):
	RESET = "\033[0m"
	PURPLE = '\033[95m'
	CYAN = '\033[37;1m' # '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[37;1n' # '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERL = '\033[4m'
	ENDC = '\033[0m'
	backBlack = '\033[40m'
	backRed = '\033[41m'
	backGreen = '\033[42m'
	backYellow = '\033[43m'
	backBlue = '\033[44m'
	backMagenta = '\033[45m'
	backCyan = '\033[46m'
	backWhite = '\033[47m'
	if "win" in sys.platform:
		RED = ""
		GREEN = ""
		YELLOW = ""
		BLUE = ""
		RESET = ""

	def __init__(self):
		"""
		simple logger untuk output text di terminal.

		example:
			>>> from lib.log import logger
			>>> msg = "aprila ganteng!"
			>>> logger.info(msg)
			[time]  INFO:  aprila ganteng!
			>>> logger.info(msg, bold_effect=True)
			[time]  INFO:  aprila ganteng!
			>>> logger.info(msg, del_levelName=True)
			[time]  aprila ganteng!

		"""
		self.now = time.strftime("%X")
		self.format = "[" + self.CYAN + '%s' + self.RED + "]>> " + self.RED + "[" + self.CYAN + '%s' + self.RED + "]"+ self.RESET
		self.format3 = "[" + self.CYAN + '%s' + self.RED + "]>> " + self.RED + "[" + self.CYAN + '%s' + self.RED + "]""[" + self.CYAN + '%s' + self.RED + ']'
		self.format4 = "[" + self.CYAN + '%s' + self.RED + "]>> " + self.YELLOW + "[" + self.CYAN + '%s' + self.YELLOW + "]>> [" + self.CYAN + '%s' + self.YELLOW + ']'
		self.format4 += "[" + self.CYAN + '%s' + self.YELLOW+ ']'
		self.format1 = "[" + self.CYAN + '%s' + self.RED + "]>>"+self.CYAN+'%s' + self.RESET
		self.format2 = "[" + self.CYAN + '%s' + self.RED + "]>> "+self.CYAN+'%s' + '\t%s' +self.RESET

	def info(self, msg, bold_effect=False, del_levelName=False):
		ln = "INFO"
		outData = self.RED + self.format % (ln, msg)
		outData += self.RESET
		print (outData)


	def sukses(self, msg, bold_effect=False, del_levelName=False):
		ln = self.GREEN+"OK"
		outData = self.RED + self.format % (msg, ln)
		outData += self.RESET
		print (outData)

	def error(self, msg, bold_effect=False, del_levelName=False):
		ln = "X"
		outData = self.RED + self.format % (msg, ln)
		outData += self.RESET
		print (outData)

	def attack(self, msg):
		ln = "*"
		outData = self.RED + self.format % (ln, msg)
		outData += self.RESET
		print (outData)
	def attacksukses(self, msg):
		ln = "*"
		msg1 = self.GREEN+"OK"
		outData = self.RED + self.format3 % (ln, msg, msg1)
		outData += self.RESET
		print (outData)
	def attacksukses1(self, msg, msg2):
		ln = "*"
		msg1 = self.GREEN+"OK"
		outData = self.RED + self.format4 % (ln, msg, msg2, msg1)
		outData += self.RESET
		print (outData)
	def error1(self, msg, msg2, bold_effect=False, del_levelName=False):
		ln = self.RED+"X"
		msg1 = "*"
		outData = self.RED + self.format4 % (msg1, msg, msg2, ln)
		outData += self.RESET
		print (outData)


	def warn(self, msg, bold_effect=False):
		YELLOW = self.YELLOW
		if bold_effect:
			YELLOW = self.YELLOW.replace("0","01")
		format = self.format.replace(" %s: ","")
		outData = YELLOW + format % (self.now, msg)
		outData += self.RESET
		print (outData)


	def debug(self, msg, bold_effect=False):
		BLUE = self.BLUE
		if bold_effect:
			BLUE = self.BLUE.replace("0","01")
		format = self.format.replace(" %s: ","")
		outData = BLUE + format % (self.now, msg)
		outData += self.RESET
		print (outData)


	def multi(self, msg, msg1, bold_effect=False, del_levelName=False):
		outData = self.RED + self.format % (msg, msg1)
		outData += self.RESET
		print (outData)

	def single(self, msg, msg1, bold_effect=False, del_levelName=False):
		outData = self.RED + self.format1 % (msg, msg1)
		outData += self.RESET
		print (outData)

	def single1(self, msg, msg1, msg2, bold_effect=False, del_levelName=False):
		outData = self.RED + self.format2 % (msg, msg1, msg2)
		outData += self.RESET
		print (outData)
	def fbdec(self, msg, msg1, msg2, bold_effect=False, del_levelName=False):
		ln = 'OK'
		outData = self.RED + self.format4 % (msg, msg1, msg2, ln)
		outData += self.RESET
		print (outData)
logger = logger()
