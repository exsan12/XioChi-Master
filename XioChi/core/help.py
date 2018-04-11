#!/usr/bin/env python
'''
Module for Remote Desktop Exploit With Metasploit Framework
Created by ~xGans
Facebook : https://web.facebook.com/ichsan.AndroSec
Gmail : Exsandrrt01@gmail.com
you can report bug on my email
'''
from core import wcolors
from time import sleep
def help():
    print "\n"
    print ("Commands\t\tDescription")
    print (wcolors.color.RED + "---------------\t\t----------------" + wcolors.color.ENDC)
    print "set \t\t\tSet Value Of Options To Modules"
    print "run \t\t\tExecute Module"
    print "use \t\t\tSelect Module For Use"
    print "os \t\t\tRun Linux Commands(ex : os ifconfig)"
    print "back\t\t\tExit Current Module"
    print "show modules\t\tShow Modules of Current Database"
    print "show options\t\tShow Current Options Of Selected Module"
    print "about\t\t\tAbout US"
    print ""
