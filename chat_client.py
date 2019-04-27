import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receiving(name, sock):
	while not shutdown:
		try:
			tLock.acquire()
			while True:
				data, addr = sock.recvfrom(1024)
				print str(data)

		except:
				pass
		finally:
				tLock.release()

host = '127.0.0.1'
port = 0

server = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receiving, args=("RecvThread", s))
rT.start()

alias = raw_input("Name: ")
#message = raw_input(alias + "->")
message = ''
while message != 'q':
	#message = raw_input(alias + "->")
	choice = raw_input(alias + "-> cmd or msg : ")
	message = raw_input(alias + "->")
	if message != '':
		#print message
		s.sendto(alias + ": " + choice + ": " + message, server)
	tLock.acquire()
	
	tLock.release()
	time.sleep(0.2)

shutdown = True
rT.join()
s.close()

