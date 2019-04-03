import socket,thread
def send():
    	rec_ip="192.168.1.4"
    	rec_port=6544   #  port >6000  are generally free to use 
    	#  calling  UDP  protocol 
    	#socket.AF_INET--->ipv4  , socket.SOCK_DGRAM--->  UDP 
    	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
     
    	#  sending  messag to target 
     
    	while  True:
    		data=raw_input("Type your message : ")
    		s.sendto(data,(rec_ip,rec_port))
    		#  this is for receiving from  sender 
    	    #  print  s.recvfrom(10)
def recv():
    	rec_ip="192.168.1.4"
    	rec_port=6544  #  port >6000  are generally free to use 
    	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    	s.bind(("",rec_port))    # proving  a way to connect 
     
    	while  True :
    		rec_data=s.recvfrom(100) 
    		print   "data rec from  client :   ",rec_data[0]
    		#rply=raw_input("enter your rply  :   ")
    	    #s.sendto(rply,rec_data[1])
     
thread.start_new_thread(recv,())
thread.start_new_thread(send,())

while True:
    pass