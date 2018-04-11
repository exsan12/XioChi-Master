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
from metamodules.scanner import vulnfinder
options = ["cgitest", "http://test.com/"]
def vulnfinderrun():
    try:
        line_1 = wcolors.color.RED + "[" + wcolors.color.CYAN + "XioChi" + wcolors.color.RED + "]" +  wcolors.color.ENDC
        line_1 += wcolors.color.RED + "[" + wcolors.color.CYAN + "Vulnerability Finder" + wcolors.color.RED + "]>> " + wcolors.color.ENDC
        com = raw_input(line_1)
        if com[0:8] =='set type':
            dork = com[9:40]
            options[0] = dork
            print wcolors.color.RED + "[" + wcolors.color.CYAN + "Type" + wcolors.color.RED + "]>> " +wcolors.color.YELLOW+ options[0]
            vulnfinderrun()
        elif com[0:10] =='set target':
            pages = com[11:99999]
            options[1] = pages
            print wcolors.color.RED + "[" + wcolors.color.CYAN + "Target" + wcolors.color.RED + "]>> " +wcolors.color.YELLOW+ options[1]
            vulnfinderrun()
        elif com[0:12] =='show options':
            print(wcolors.color.YELLOW + 26 * "#" +wcolors.color.RED+"[ Options List ]"+wcolors.color.YELLOW+ 26 * "#")
            print wcolors.color.CYAN+"Options\t\t Value\t\t\t Description"
            print wcolors.color.RED+"---------\t--------------\t\t------------------"
            print wcolors.color.CYAN+"Type\t\t"+options[0]+"\t\tSelect Type"
            print "Type: <list> for see the type"
            print "Target\t\t"+options[1]+"\t\t\tYour Target"
            print(wcolors.color.YELLOW + 68 * "#"+wcolors.color.ENDC)
            vulnfinderrun()
        elif com[0:2] =='os':
            log.logger.single("Command Executed", "\n"+wcolors.color.CYAN)
            os.system(com[3:])
            vulnfinderrun()
        elif com[0:4] =='help':
            help.help()
            vulnfinderrun()
        elif com[0:4] =='back':
            pass
        elif com[0:4] =='list':
            log.logger.info("List Type:")
            print '\n'
            print wcolors.color.CYAN +"cgitest (Test On web Cgi)"
            print "wptest (wordpress find param and info explodb)"
            print "weblogictest (Tested On WebLogic)"
            print "dirtravwintest (DirTraversalWin Finder)"
            print "dirtravunixtest (DirTraversalUnix Finder)"
            print "tomcattest (Tested On Tomcat site)"
            print "apachetest (Test Brute DirecVuln)"+wcolors.color.ENDC
            print ""
            vulnfinderrun()
        elif com[0:5] =='about':
            about.about()
            vulnfinderrun()
        elif com[0:3] =='run':
            if options[0] =='cgitest':
                log.logger.attacksukses1("Testing Target",options[1])
                vulnfinder.cgivuln(options[1])
                vulnfinderrun()
            elif options[0] =='wptest':
                log.logger.attacksukses1("Testing Target",options[1])
                vulnfinder.wpvuln(options[1])
                vulnfinderrun()
            elif options[0] =='dirtravwintest':
                log.logger.attacksukses1("Testing Target",options[1])
                vulnfinder.dirtraversalwin(options[1])
                vulnfinderrun()
            elif options[0] =='dirtravunixtest':
                log.logger.attacksukses1("Testing Target",options[1])
                vulnfinder.dirtraversalunix(options[1])
                vulnfinderrun()
            elif options[0] =='weblogictest':
                log.logger.attacksukses1("Testing Target",options[1])
                vulnfinder.weblogic(options[1])
                vulnfinderrun()
            elif options[0] =='apachetest':
                log.logger.attacksukses1("Testing Target",options[1])
                vulnfinder.apache(options[1])
                vulnfinderrun()
            elif options[0] =='tomcattest':
                log.logger.attacksukses1("Testing Target",options[1])
                vulnfinder.tomcat(options[1])
                vulnfinderrun()
            else:
                print wcolors.color.RED + "[" + wcolors.color.CYAN + "Type NotFound!!" + wcolors.color.RED + "]>> " + com
                vulnfinderrun()
        else:
            print wcolors.color.RED + "[" + wcolors.color.CYAN + "Wrong Command" + wcolors.color.RED + "]>> " + com
            vulnfinderrun()
    except(KeyboardInterrupt):
        print ""
