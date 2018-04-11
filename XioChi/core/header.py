#!/usr/bin/env python

import time, sys, random
colors = [31, 37]
clear = "\x1b[0m"

def main_header():
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	colran = random.randint(1, 7)
	color_num = colran
	if color_num ==1:
		warna = RED
	if color_num ==2:
		warna = DARKCYAN
	if color_num ==3:
		warna = BLUE
	if color_num ==4:
		warna = CYAN
	if color_num ==5:
		warna = YELLOW
	if color_num ==6:
		warna = BOLD + RED
	if color_num ==7:
		warna = PURPLE
	header_r = r"""
  ###          ##                           ######      /
 /####       ####  /   ##                  /  /###  / #/        ##
/   ###      /####/   ###                 /  /  ###/  ##       ###
     ###    /   ##    ##                 /  ##   ##   ##       ##
      ###  /                           /  ###        ##
       ###/         ###       /###    ##   ##        ##  /## ###
        ###          ###     / ###  / ##   ##        ## / ### ###
        /###          ##    /   ###/  ##   ##        ##/   ### ##
       /  ###         ##   ##    ##   ##   ##        ##     ## ##
      /    ###        ##   ##    ##   ##   ##        ##     ## ##
     /      ###       ##   ##    ##    ##  ##        ##     ## ##
    /        ###      ##   ##    ##     ## ##      / ##     ## ##
   /          ###   / ##   ##    ##      ###     /   ##     ## ##
  /            ####/  ### / ######        ######/    ##     ## ### /
 /              ###    ##/   ####           ###       ##    ##  ##/
                                                            /
                                                           /
                                                          /
                                                         /                    """
	# print str(warna) + header_r
	for N, line in enumerate(header_r.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
		time.sleep(0.05)
