import thread 
import os
def one():
	while True:
		print 'hello'
		
def two():
	while True:
		print 'world'

thread.start_new_thread(one,())
thread.start_new_thread(two,())

while True:
	pass
