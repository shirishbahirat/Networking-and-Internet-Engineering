#!/usr/bin/python
"""
	getquote.py

	This program contacts an internet financial service to 
	learn the current price for Intel Corporation's stock.

	programmer: ALLAN CRUSE
	written on: 01 JAN 2009
"""

import socket

try:
	host = "download.finance.yahoo.com"
	port = 80

	sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	sock.settimeout( 1 )
	sock.connect( ( host, port ) )
	sock.send( "GET /d/quotes.csv?s=INTC&f=sl1d1t1c1&e=.csv \r\n" )
 	sock.send( "\r\n" )
	response_string, server = sock.recvfrom( 4096 )
	quote = str.split( response_string, ',' )	

except	socket.error, msg:
	print "An error occurred:", msg

else:
	print
	print "Intel Stock:", '$'+quote[1], "at", quote[3], "on", quote[2]  
	print
