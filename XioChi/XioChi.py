#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
'''
Created by AndroSec1337 Cyber Team
Author : ~xGans - Mr_Siln7 - ./Xi4u7
Thx To : Deadrz_404 - Dro!der_404 - Mr.b0t4k - Mr_/bon'007 - Elang X-CoderID - C4bnl - V-Z3R0 - 6hosthere502 - Mr.BrPing And All Member AndroSec1337 Cyber Team
Fanspage : https://facebook.com/androsec1337cyberteam
Website : http://androsec1337.org/
'''
import os, sys
from time import sleep
from subprocess import *
import subprocess
try:
    from core import *
    from core.wcolors import color
    from core import about
    from core import help
    from core import modules_database
    from core import log

    # Import Scanners Modules
    from metamodules.scanner import dirbrute
    from metamodules.scanner import admin_panel
    from metamodules.scanner import dorkgrablink
    from metamodules.scanner import vulnfinderrun
    from metamodules.scanner import vulnfinder

    # Import Exploit Modules
    from metamodules.exploit import mp4xploit
    from metamodules.exploit import RDPexploit
    # Import Other Modules
    from metamodules.other import emailfilter
    from metamodules.other import csrfcreated

    # Import webapps Wordpress Exploit
    from metamodules.webapps.wordpress import InBoundioMarketing as ibm
    from metamodules.webapps.wordpress import dzszoomsounds as dzs
    from metamodules.webapps.wordpress import downloadmanager as dwn
    from metamodules.webapps.wordpress import HdWebPlayerSql as hwps
    from metamodules.webapps.wordpress import learndash1

    # Import WebApps Joomla Exploit
    from metamodules.webapps.joomla import com_b2jcontact

    #  Import Reverse Enginer Tools
    from metamodules.reversenginer.decoder import pyc_decompiler

except Exception as err:
	print color.RED + "[" + color.CYAN +"Error : "+str(err) + color.RED + "]" + color.ENDC
	sys.exit()

except KeyboardInterrupt:
	print color.RED + "[" + color.CYAN + "Fail To Import" + color.RED + "]"
	exit(1)

def main():
    try:
        line_1 = color.RED + "["+color.CYAN+"XioChi"+color.RED+"] >> "+color.ENDC
        terminal = raw_input(line_1)
        terminal = terminal.lower()
        if terminal[0:3] =='use':
            if terminal[4:30] =='exploit/remote_desktop':
                RDPexploit.rdpexploit()
                main()
            if terminal[4:30] =='scanner/google_dork':
                dorkgrablink.dorkgrablink()
                main()
            if terminal[4:30] =='filter/email_list':
                emailfilter.emailfilter()
                main()
            if terminal[4:30] =='csrf/hijacking':
                csrfcreated.csrfcreated()
                main()
            elif terminal[4:30] =='scanner/dir_brute':
                dirbrute.dirbrute()
                main()
            elif terminal[4:30] =='scanner/admin_panel':
                admin_panel.admin()
                main()
            elif terminal[4:30] =='scanner/vulnfinder':
                vulnfinderrun.vulnfinderrun()
                main()
            elif terminal[4:30] =='exploit/stagefright':
                mp4xploit.mp4exploit()
                main()
            elif terminal[4:30] =='exploit/csrf_maker':
                csrfcreated.csrfcreated()
                main()
            elif terminal[4:99] =='wordpress/inboundiomarketing':
                ibm.ibm()
                main()
            elif terminal[4:99] =='wordpress/dzszoomsounds':
                dzs.dzs()
                main()
            elif terminal[4:99] =='wordpress/downloads_manager':
                dwn.dwnm()
                main()
            elif terminal[4:99] =='wordpress/learndash_v1':
                hwps.hd()
                main()
            elif terminal[4:99] =='wordpress/hdwebplayersql':
                hwps.hd()
                main()
            elif terminal[4:99] =='joomla/com_b2jcontact':
                com_b2jcontact.b2j()
                main()
            elif terminal[4:99] =='reversenginer/pyc_decompiler':
                pyc_decompiler.pyc_deco()
                main()
            else:
                print color.RED + "[" + color.CYAN + "Unknow Module" + color.RED + "]>> ", terminal[4:99]
                main()
        elif terminal[0:12] == 'show modules':
            modules_database.modules_database()
            main()
        elif terminal[0:4] =='help':
            help.help()
            main()
        elif terminal[0:2] =='os':
            log.logger.single("Command Executed", "\n"+color.CYAN)
            os.system(terminal[3:])
            print ""
            main()
        elif terminal[0:5] =='about':
            about.about()
            main()
        elif terminal[0:4] =='exit':
            exit()
        else:
            print color.RED + "[" + color.CYAN + "Wrong Command" + color.RED + "]>> ", terminal
            main()
    except(KeyboardInterrupt):
        print(color.RED + "\n[*] (Ctrl + C ) Detected, Trying To Exit ..." + color.ENDC)
        print(color.YELLOW + "[*] Thank For Using my Pentest Tools ^~^" + color.ENDC)
def start():
	about.about()
	main()
if __name__=='__main__':
    start()
