#!usr/bin/env python2

import socket

recv_ip="127.0.0.1"

recv_port=9090 #port >6000 are free to use

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((recv_ip,recv_port))


while  True :
	#it will rcv data from client /sender and its socket as well
	msg = raw_input ("enter message: ")
	s.sendto(msg,rec_data[1])
	rec_data =s.recvfrom(100)
	print "data rcv from client : ",rec_data[0]
	#here rec_data[1] is client ip and port combo
	rply = raw_input ("enter reply: ")
	s.sendto(rply,rec_data[1])
