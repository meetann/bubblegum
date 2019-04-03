#!/usr/bin/env python2

import  socket

rec_ip="192.168.1.5"
rec_port=21219   #  port >6000  are generally free to use 

#  calling  UDP  protocol 
#             socket.AF_INET--->ipv4         , socket.SOCK_DGRAM--->  UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# ================================ above this section is common for both sender /receiver

#   rec side only 
#  binding ip and port 
s.bind(("",rec_port))            # proving  a way to connect 

while  True	 :
		# it will rec data from client / sender and its socket as well
	rec_data=s.recvfrom(100) 
	print   "data rec from  client :   ",rec_data[0]
#    here  rec_data[1]  is  client ip and client port combo
	rply=raw_input("enter your rply  :   ")
	s.sendto(rply,rec_data[1])
