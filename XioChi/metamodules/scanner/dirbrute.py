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
import requests
options = ["http://test.com/", 'core/wordlist/vulns/cgivulnerabledir.txt']
def dirbrute():
    try:
        line_1 = wcolors.color.RED + "[" + wcolors.color.CYAN + "XioChi" + wcolors.color.RED + "]" +  wcolors.color.ENDC
        line_1 += wcolors.color.RED + "[" + wcolors.color.CYAN + "scanner/dir_brute" + wcolors.color.RED + "]>> " + wcolors.color.ENDC
        com = raw_input(line_1)
        if com[0:10] =='set target':
            dork = com[11:9999]
            options[0] = dork
            print wcolors.color.RED + "[" + wcolors.color.CYAN + "TARGET" + wcolors.color.RED + "]>> " +wcolors.color.YELLOW+ options[0]
            dirbrute()
        elif com[0:12] =='set wordlist':
            dork = com[13:9999]
            options[1] = dork
            print wcolors.color.RED + "[" + wcolors.color.CYAN + "WORDLIST" + wcolors.color.RED + "]>> " +wcolors.color.YELLOW+ options[1]
            dirbrute()
        elif com[0:12] =='show options':
            print wcolors.color.CYAN+"Options\t\t Value\t\t\t Description"
            print wcolors.color.RED+"---------\t--------------\t\t------------------"
            print wcolors.color.CYAN+"Target\t\t"+options[0]+"\t\tTarget"
            print wcolors.color.CYAN+"Wordlist\t"+options[1]+"\t\tWordlist default is in Value more wordlist(core/wordlist/)"
            dirbrute()
        elif com[0:2] =='os':
            log.logger.single("Command Executed", "\n"+wcolors.color.CYAN)
            os.system(com[3:])
            dirbrute()
        elif com[0:4] =='help':
            help.help()
            dirbrute()
        elif com[0:4] =='back':
            pass
        elif com[0:5] =='about':
            about.about()
            dirbrute()
        elif com[0:3] =='run':
            log.logger.info("Checking Wordlist..!!")
            sleep(1)
            try:
                log.logger.sukses("File Found")
                aol = set(open(options[1]).readlines())
                open(options[1], 'w').writelines(set(aol))
                log.logger.attacksukses1("List Total", len(list(aol)))
                sleep(1)
                s = open(options[1], 'r')
                log.logger.attack("Starting BruteForce")
                save = open('output/dirbruteList.txt', 'a')
                for i in s.readlines():
                    try:
                        p = options[0] + '/' + i.strip()
                        r = requests.get(p)
                        try:
                            if r.status_code in (200, 302):
                                log.logger.attacksukses1("Dir Found",str(p))
                                save.write("\n"+'['+"Website"+"]>>"+"["+options[0]+']'+'\n'+str(p)+"\n")
                            else:
                                log.logger.error1("Not Found", wcolors.color.RED+str(p))
                        except(KeyboardInterrupt):
                            print ""
                    except(requests.exceptions.InvalidSchema):
                        log.logger.error("Invalid URL >>"+options[0])
                        sleep(1)
                        admin()
                    except(requests.exceptions.SSLError):
                        log.logger.error("SSL Error...We cant visit this website with much request")
                        log.logger.error("Please Wait Delay...")
                        sleep(10)
                    except(requests.exceptions.ConnectionError):
                        log.logger.error("Connection Error <Failed to establish a new connection>")
                    except(requests.exceptions.MissingSchema):
                        log.logger.error("Please Using http:// or https://")
                        sleep(1)
                        dirbrute()
                    except(KeyboardInterrupt):
                        print ""
                save.close()
                aol = set(open('output/dirbruteList.txt').readlines())
                open('output/dirbruteList.txt', 'w').writelines(set(aol))
                log.logger.attacksukses1("Saved On", 'output/dirbruteList.txt')
                log.logger.attacksukses("Done..!!")
            except(KeyboardInterrupt):
                print ""
            except IOError:
                log.logger.error("File NotFound")
            dirbrute()
        else:
            print wcolors.color.RED + "[" + wcolors.color.CYAN + "Wrong Command" + wcolors.color.RED + "]>> " + com
            dirbrute()
    except(KeyboardInterrupt):
        print ""
