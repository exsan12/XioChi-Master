# custom class to Loading animation like msfconsole
# by mr_silen7 :v
import sys
import time
import os
from threading import Thread
import log
class Loading(Thread):
    def __init__(self, messages):

        Thread.__init__(self)
        self.messages = messages
        self.setRunning = True

    def run(self):
        while self.setRunning:
            for x in range(len(self.messages)):
                sys.stdout.write('\r'+log.RED+'['+log.CYAN+'*'+log.RED+'] ['+log.CYAN+self.messages[:x]+self.messages[x:].capitalize()+log.RED+']')
                sys.stdout.flush()
                time.sleep(0.1)
                try:
                    sys.stdout.write('\r'+"\t")
                except(KeyboardInterrupt):
                    print ""
