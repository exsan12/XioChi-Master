#!/usr/bin/env python
'''
Module for Remote Desktop Exploit With Metasploit Framework
Created by ~xGans
Facebook : https://web.facebook.com/ichsan.AndroSec
Gmail : Exsandrrt01@gmail.com
you can report bug on my email
'''
from core import log
import os
from core import header
from core import wcolors
def add():
    header.main_header()
def about():
    os.system('clear')
    add()
    msg = "Devlopers" + wcolors.color.ENDC
    web1 = "Website  "
    web = "Patner   "
    fpp = "Fanspage "
    msg1 = " ~xGans - Mr_Siln7 - ./Xi4u7 "+ wcolors.color.ENDC
    msgg = "Thanks To" +wcolors.color.ENDC
    msgg1 = " Deadrz_404 - Dro!der_404 - Mr.b0t4k_47 - Mr_/bon'007 " + wcolors.color.ENDC
    fb = " https://web.facebook.com/androsec1337cyberteam "
    site = " http://androsec1337.org/ "
    site2 = " http://sincansec.blogspot.com/ "
    print "\n"
    log.logger.multi(msg, msg1)
    log.logger.multi(msgg, msgg1)
    log.logger.multi(fpp, fb)
    log.logger.multi(web1, site2)
    log.logger.multi(web, site)
    print ""
    log.logger.attacksukses1("Note", "#")
    log.logger.attack("use for educational purpose only")
    log.logger.attack("I Create This Tools Just For Educational and Test On Your Own site")
    print "\n"
