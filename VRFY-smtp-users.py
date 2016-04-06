#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
	print "USAGE: <ip> <username>"
	sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# Create a Socket
connect=s.connect((sys.argv[1], 25))			# Connect to server
banner=s.recv(1024)					# Receive the banner
print banner
s.send('VRFY ' + sys.argv[2] + '\r\n')			# VRFY a user
result=s.recv(1024)
print result
s.close()						# Close socket
