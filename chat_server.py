import socket
import time
import subprocess

host = '127.0.0.1'
port = 5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quitting = False
print "Server Started."

while not quitting:
	try:
			data, addr = s.recvfrom(1024)
			#print str(data)
			if 'Quit' in str(data):
				quitting = True

			if addr not in clients:
				clients.append(addr)

			returned_value=''
			returned_output=''
			if data:
				cmd=data.rsplit(':', 1)[1]
				#print d
				returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
				print('returned value:', returned_value)
				try:
					returned_output = subprocess.check_output(cmd)
					print('o/p:', returned_output.decode("utf-8"))
				except:
					print('Wrong linux command')

			if 'q' in str(data):
				user=data.rsplit(':', 1)[0]
				print time.ctime(time.time()) + str(addr) + ": :" + str(user) + " left"  
			
			else:
				print time.ctime(time.time()) + str(addr) + ": :" + str(data)
				if(returned_value):
					s.sendto('NOACK', addr)
				else:
					s.sendto('ACK', addr)
			#for client in clients:
			#	s.sendto(data, client)


	except:
			pass

s.close()
