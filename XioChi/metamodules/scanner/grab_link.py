"""Google Dork Grab link
Recoded From Marksman
Author : xGans
Usage:
  scrap.py <search> <pages>
  scrap.py (-h | --help)

Arguments:
  <search>  String to be Searched
  <pages>   Number of pages

Options:
  -h, --help     Show this screen.

"""
import  requests, re
from    docopt import docopt
from    bs4 import BeautifulSoup
from    time import time as timer
import os,sys,thread,socket
import time
import subprocess

#********* CONSTANT VARIABLES *********
BACKLOG = 50            # how many pending connections queue will hold
MAX_DATA_RECV = 4096    # max number of bytes we receive at once
DEBUG = False           # set to True to see the debug msgs

#********* MAIN PROGRAM ***************
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERL = '\033[4m'
ENDC = '\033[0m'
backBlack = '\033[40m'
backRed = '\033[41m'
backGreen = '\033[42m'
backYellow = '\033[43m'
backBlue = '\033[44m'
backMagenta = '\033[45m'
backCyan = '\033[46m'
backWhite = '\033[47m'
Info = RED + "[" + CYAN + "INFO" + RED + "]>> "
bes = 'output/Grab_link.txt'
def get_urls(search_string, start):
    #Empty temp List to store the Urls
    temp        = []
    url         = 'http://www.google.com/search'
    payload     = { 'q' : search_string, 'start' : start }
    my_headers  = { 'User-agent' : 'Mozilla/11.0' }
    r           = requests.get( url, params = payload, headers = my_headers )
    soup        = BeautifulSoup( r.text, 'html.parser' )
    h3tags      = soup.find_all( 'h3', class_='r' )
    for h3 in h3tags:
        try:
            temp.append( re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1) )
        except:
            continue
    return temp

def main():
    start     = timer()
    #Empty List to store the Urls
    result    = []
    arguments = docopt( __doc__, version='Google Grab Link' )
    search    = arguments['<search>']
    pages     = arguments['<pages>']
    #Calling the function [pages] times.
    for page in range( 0,  int(pages) ):
        #Getting the URLs in the list
        result.extend( get_urls( search, str(page*10) ) )
    #Removing Duplicate URLs
    result = list( set( result ) )
    count = 1
    for list1 in result:
        msg = RED+"["+CYAN+str(count)+RED+"]>> ["+CYAN+str(list1)+RED+"]"
        print msg
        count += 1
        c = open(bes, 'a')
        c.write(str(list1) + "\n")
        c.close()
    now = time.strftime("%X")
    print( Info + YELLOW+"Total URLs Scraped : "+RED+"["+CYAN+" {0} ".format(len( result )) +RED+"]")
    print( Info + YELLOW+"Script Execution Time : "+RED+"["+CYAN+" {0} ".format( timer() - start, ) +RED+"]")
    asdas = subprocess.check_output('echo [ ${PWD}/%s ]' %bes, shell=True)
    print RED + "[" + CYAN + "Saved" + RED + "]>> " + YELLOW + str(asdas)
if __name__ == '__main__':
    main()
