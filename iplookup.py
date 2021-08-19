#!/usr/bin/python
"""
	iplookup.py

	This program illustrates the use of the 'try/except' construct
	in the Python language to report the Internet Protocol address 
	for the domain or host whose name is entered as a command-line
	argument, or for the 'localhost' if no arguments are supplied.

	      execute using:  $ python ./iplookup.py <hostname>

	programmer: ALLAN CRUSE
	written on: 04 JAN 2008
"""

import sys, socket

try:
	hostname = sys.argv[1]
except: 
	hostname = "localhost"

try:
	hostip = socket.gethostbyname( hostname )
except: 
	hostip = "unknown"

print "The IP-address for \'" + hostname + "\' is " + hostip


