#!usr/bin/env python2

import socket
import thread 

def send() :
	recv_ip="127.0.0.1"

	recv_port=9090 #port >6000 are free to use

	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	#sending message to target

	while True:
		data=raw_input("Type : ")
	        #it will send data to rcvr as well as create own                socket (own ip and any random port)
		s.sendto(data,(recv_ip,recv_port))
		print s.recvfrom(100)

thread.start_new_thread(send,())

while True:
	pass
