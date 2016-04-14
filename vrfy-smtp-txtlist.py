#!/usr/bin/python
#takes an ip as a parameter
#verify users in users.txt from smtp server

import socket
import sys

if len(sys.argv) != 3:
	print "USAGE: <ip> <list.txt>"
	sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# Create a Socket
connect=s.connect((sys.argv[1], 25))			# Connect to server
banner=s.recv(1024)					# Receive the banner
print banner
with open(sys.argv[2]) as f:
	for line in f:
		#print line
		s.send('VRFY ' + line + '\r')			# VRFY a user
		result=s.recv(1024)
		print result
		if 'str' in line:
			break
s.close()						# Close socket
