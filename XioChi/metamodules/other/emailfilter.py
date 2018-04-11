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
from core import log
from time import sleep
from pathlib import Path
import re
from core import about
options = ["metamodules/listall.txt"]
def emailfilter():
    try:
        line_1 = wcolors.color.RED + "[" + wcolors.color.CYAN + "XioChi" + wcolors.color.RED + "]" +  wcolors.color.ENDC
        line_1 += wcolors.color.RED + "[" + wcolors.color.CYAN + "Email Filter" + wcolors.color.RED + "]>> " + wcolors.color.ENDC
        com = raw_input(line_1)
        if com[0:8] =='set list':
            dork = com[9:100]
            options[0] = dork
            print wcolors.color.RED + "[" + wcolors.color.CYAN + "Email List" + wcolors.color.RED + "]>> " +wcolors.color.YELLOW+ options[0]
            emailfilter()
        elif com[0:12] =='show options':
            print(wcolors.color.YELLOW + 26 * "#" +wcolors.color.RED+"[ Options List ]"+wcolors.color.YELLOW+ 26 * "#")
            print wcolors.color.CYAN+"Options\t\t Value\t\t\t Description"
            print wcolors.color.RED+"---------\t--------------\t\t------------------"
            print wcolors.color.CYAN+"List\t\t"+options[0]+"\tList of email (on .txt)"
            print(wcolors.color.YELLOW + 68 * "#"+wcolors.color.ENDC)
            emailfilter()
        elif com[0:2] =='os':
            log.logger.single("Command Executed", "\n"+wcolors.color.CYAN)
            os.system(com[3:])
            emailfilter()
        elif com[0:4] =='help':
            help.help()
            emailfilter()
        elif com[0:4] =='back':
            pass
        elif com[0:5] =='about':
            about.about()
            emailfilter()
        elif com[0:3] =='run':
            log.logger.info("Checking Path Of List!!")
            sleep(1)
            p = Path(options[0])
            yahoo = "yahoo.com"
            gmail = "gmail.com"
            aol = "aol.com"
            hotmail = "hotmail.com"
            outlook = "outlook.com"
            count = 1
            bot = 1
            count1 = 1
            count2 = 1
            cc = 1
            try:
                text = open(options[0], 'r')
                read = text.read()
                log.logger.sukses("File Found")
                match1 = re.findall(r'[\w\.-]+@'+yahoo, read)
                match2 = re.findall(r'[\w\.-]+@'+gmail, read)
                match3 = re.findall(r'[\w\.-]+@'+hotmail, read)
                match4 = re.findall(r'[\w\.-]+@'+aol, read)
                outmail = re.findall(r'[\w\.-]+@'+outlook, read)
                alltext = re.findall(r'[\w\.-]+@[\w\.-]+', read)
                result1 = list( set( match1 ) )
                result2 = list( set( match2 ) )
                result3 = list( set( match3 ) )
                result4 = list( set( match4 ) )
                result5 = list( set( outmail ) )
                result6 = list( set( alltext ) )
                print ""
                yahoo = open('output/yahoo.txt', 'a')
                aol = open('output/aol.txt', 'a')
                hotmail = open('output/hotmail.txt', 'a')
                gmail = open('output/gmail.txt', 'a')
                out = open('output/outlook.txt', 'a')
                for yah in result1:
                    log.logger.single1(count, "[Yahoo]>>", yah)
                    count += 1
                    yahoo.write(yah+ "\n")
                for ao in result4:
                    log.logger.single1(bot, "[Aol]>>", ao)
                    bot += 1
                    aol.write(ao+ "\n")
                for hot in result3:
                    log.logger.single1(count1, "[Hotmail]>>", hot)
                    count1 += 1
                    hotmail.write(hot+ "\n")
                for notident in result5:
                    log.logger.single1(cc, "[Outlook]>>", notident)
                    cc += 1
                    out.write(notident+ "\n")
                for gma in result2:
                    log.logger.single1(count2, "[Gmail]>>", gma)
                    count2 += 1
                    gmail.write(gma+ "\n")
                gmail.close()
                yahoo.close()
                hotmail.close()
                aol.close()
                out.close()
                print '\n'
                log.logger.multi("List On", options[0])
                log.logger.multi("Yahoo", +len(result1))
                log.logger.multi("Aol", len(result4))
                log.logger.multi("Gmail", len(result2))
                log.logger.multi("Hotmail", len(result3))
                log.logger.multi("Outlook", len(result5))
                log.logger.multi("Total List", len(result1 + result2 + result3 +result4+result5))
                log.logger.multi("Total List On "+wcolors.color.RED+"["+wcolors.color.CYAN+options[0]+wcolors.color.RED+"]", len(result6))
                print ""
                log.logger.attack("Removing Duplicate Mail On Saved Folder")
                try:
                    ao = 'output/aol.txt'
                    yahu = 'output/yahoo.txt'
                    hotma = 'output/hotmail.txt'
                    gmai = 'output/gmail.txt'
                    outlu = 'output/outlook.txt'
                    aol = set(open(ao).readlines())
                    yahoo = set(open(yahu).readlines())
                    hotmail = set(open(hotma).readlines())
                    gmail = set(open(gmai).readlines())
                    outlook = set(open(outlu).readlines())
                    open(ao, 'w').writelines(set(aol))
                    open(yahu, 'w').writelines(set(yahoo))
                    open(hotma, 'w').writelines(set(hotmail))
                    open(gmai, 'w').writelines(set(gmail))
                    open(outlu, 'w').writelines(set(outlook))
                    sleep(1)
                    log.logger.attacksukses("Remove Duplicate Done")
                    log.logger.multi("Saved On", 'Xiochi/output/<here>')
                    print ""
                    log.logger.attacksukses("ReTotal All On Saved Folder")
                    sleep(1)
                    log.logger.multi("Yahoo", +len(yahoo))
                    log.logger.multi("Aol", len(aol))
                    log.logger.multi("Gmail", len(gmail))
                    log.logger.multi("Hotmail", len(hotmail))
                    log.logger.multi("Outlook", len(outlook))
                    log.logger.multi("Total List On Saved Folder", len(aol)+len(yahoo)+len(gmail)+len(hotmail)+len(outlook))
                    print "\n"
                    emailfilter()
                except KeyboardInterrupt:
                    msg = "Stopped"
                    log.logger.error(msg)
            except IOError:
                log.logger.error("File NotFound")
            except KeyboardInterrupt:
                   msg = "Stopped"
                   log.logger.error(msg)

            emailfilter()
        else:
            print wcolors.color.RED + "[" + wcolors.color.CYAN + "Wrong Command" + wcolors.color.RED + "]>>>" + com
            emailfilter()
    except(KeyboardInterrupt):
        print ""
