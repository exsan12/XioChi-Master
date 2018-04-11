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
from core import payloadcsrf
options = ["clickjacking"]
def csrfcreated():
    try:
        line_1 = wcolors.color.RED + "[" + wcolors.color.CYAN + "XioChi" + wcolors.color.RED + "]" +  wcolors.color.ENDC
        line_1 += wcolors.color.RED + "[" + wcolors.color.CYAN + "CSRF Maker" + wcolors.color.RED + "]>> " + wcolors.color.ENDC
        com = raw_input(line_1)
        if com[0:8] =='set csrf':
            dork = com[9:40]
            options[0] = dork
            print wcolors.color.RED + "[" + wcolors.color.CYAN + "CSRF" + wcolors.color.RED + "]>> " +wcolors.color.YELLOW+ options[0]
            csrfcreated()
        elif com[0:12] =='show options':
            print(wcolors.color.YELLOW + 26 * "#" +wcolors.color.RED+"[ Options List ]"+wcolors.color.YELLOW+ 26 * "#")
            print wcolors.color.CYAN+"Options\t\t Value\t\t\t Description"
            print wcolors.color.RED+"---------\t--------------\t\t------------------"
            print wcolors.color.CYAN+"crsf\t\t"+options[0]+"\tCRSF Type Want To Create"
            print(wcolors.color.YELLOW + 68 * "#"+wcolors.color.ENDC)
            csrfcreated()
        elif com[0:2] =='os':
            log.logger.single("Command Executed", "\n"+wcolors.color.CYAN)
            os.system(com[3:])
            csrfcreated()
        elif com[0:4] =='help':
            help.help()
            csrfcreated()
        elif com[0:4] =='back':
            pass
        elif com[0:5] =='about':
            about.about()
            csrfcreated()
        elif com[0:4] =='list':
            print wcolors.color.CYAN+"clickjacking (Sorry Next Update Will Much More)"
            csrfcreated()
        elif com[0:3] =='run':
            if options[0] =='clickjacking':
                xssc = 'XSS'
                line_2= line_1 + wcolors.color.RED + "[" + wcolors.color.CYAN + "%s CODE"%(xssc) + wcolors.color.RED + "]>> " + wcolors.color.ENDC
                xss = raw_input(line_2)
                ifrm = 'IFRAME'
                line_3 = line_1 + wcolors.color.RED + "[" + wcolors.color.CYAN + "%s CODE"%(ifrm) + wcolors.color.RED + "]>> " + wcolors.color.ENDC
                iframe = raw_input(line_3)
                sss = iframe.replace('\n', '')
                payloadcsrf.clickjacking(xss, iframe)
            else:
                log.logger.error("Your Options CSRF Not Found<Sorry My Payload Just Click Jacking...Wait Next Update :)")
            csrfcreated()
        else:
            print wcolors.color.RED + "[" + wcolors.color.CYAN + "Wrong Command" + wcolors.color.RED + "]>> " + com
            csrfcreated()
    except(KeyboardInterrupt):
        print ""
