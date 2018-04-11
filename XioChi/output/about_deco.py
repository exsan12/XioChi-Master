# uncompyle6 version 3.1.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.12 (default, Dec  5 2016, 05:42:51) 
# [GCC 4.9 20140827 (prerelease)]
# Embedded file name: /storage/sdcard1/Project/Xiochi/core/about.py
# Compiled at: 2018-03-31 12:03:58
"""
Module for Remote Desktop Exploit With Metasploit Framework
Created by ~xGans
Facebook : https://web.facebook.com/ichsan.AndroSec
Gmail : Exsandrrt01@gmail.com
you can report bug on my email
"""
from core import log
import os
from core import header
from core import wcolors

def add():
    header.main_header()


def about():
    os.system('clear')
    add()
    msg = 'Devlopers' + wcolors.color.ENDC
    web1 = 'Website  '
    web = 'Patner   '
    fpp = 'Fanspage '
    msg1 = ' ~xGans - Mr_Siln7 - ./Xi4u7 ' + wcolors.color.ENDC
    msgg = 'Thanks To' + wcolors.color.ENDC
    msgg1 = " Deadrz_404 - Dro!der_404 - Mr.b0t4k_47 - Mr_/bon'007 " + wcolors.color.ENDC
    fb = ' https://web.facebook.com/androsec1337cyberteam '
    site = ' http://androsec1337.org/ '
    site2 = ' http://sincansec.blogspot.com/ '
    print '\n'
    log.logger.multi(msg, msg1)
    log.logger.multi(msgg, msgg1)
    log.logger.multi(fpp, fb)
    log.logger.multi(web1, site2)
    log.logger.multi(web, site)
    print '\n'