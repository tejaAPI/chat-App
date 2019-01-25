import socket
import threading

count=0

sock=socket.socket()
all_connections=[]
address=[]
req_threads=[]

def init():
	sock.bind(('0.0.0.0',10000))
	sock.listen(100)
	
def request(c):
	
	
	while True:
			
			cmd=all_connections[c].recv(1024)
			cmd=cmd.decode()
			
			if str(cmd)=='list':
				send_connections(c)
	

def connections():
	global count
	while True:
		c, a=sock.accept()
		
		all_connections.append(c)
		address.append(a)
		if(c):
			
			create_thread(count)
			count+=1
			
		print(c)


def create_thread(c):
	
	t=threading.Thread(target=request,args=(c,))
	req_threads.append(t)
	t.deamon=True
	t.start()
	
	
			
				
def accepting_connections():
	cThread=threading.Thread(target=connections)
	cThread.deamon=True
	cThread.start()
	

def send_connections(c):
	
	all_connections[c].send(bytes(str(address),'utf-8'))


       
			
def main():
	init()
	accepting_connections()
	
	
	
main()
