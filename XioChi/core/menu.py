#!/usr/bin/env python
'''
Module for Remote Desktop Exploit With Metasploit Framework
Created by ~xGans
Facebook : https://web.facebook.com/ichsan.AndroSec
Gmail : Exsandrrt01@gmail.com
you can report bug on my email
'''
from core import wcolors
from core import log
def main_info():
	ston = wcolors.color.BLUE + "[" + wcolors.color.ENDC
	msg = "XioChi Author" + wcolors.color.ENDC
	msg1 = " ~xGans & Thanks To Mr_/bon'007 & Mr_Siln7"+ wcolors.color.ENDC
	facbok = "https://web.facebook.com/ichsan.AndroSec"
	facebook = "Facebook"
	code = "Program "
	print "\n\n"
	log.logger.multi(msg, msg1)
	log.logger.single1(facebook, facbok, "")
	log.logger.single1(code, "Python", "")
	log.logger.single1("Team    ", "AndroSec1337", "")
	log.logger.single1("BlogSpot   ", "https://sincansec.blogspot.com", "")
	print "\n\n"
