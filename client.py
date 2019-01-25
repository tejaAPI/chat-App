import socket
import threading
import sys

sock=socket.socket()
address=sys.argv[1]	
'''def sendMsg():
	while True:
		
		sock.send(bytes(input(),'utf-8'))
		
		
def recvMsg():
	while True:
		data=sock.recv(1024)
		if len(data)>0:
			print("Message from ",address,">"+str(data,"utf-8")+"\n",end="")
	'''		
		
def init(address):
	try:
		sock.connect((address,10000))
		print("Connected")
	except:
		print("Not Connected")
	

def list_connections(cmd):
	sock.send(str.encode(cmd))
	Friends_list=sock.recv(1024)
	Friends_list=Friends_list.decode("utf-8")
	
	print(Friends_list[1:-1],end="\n")
	

def start_chat():

	while True:
		cmd = input('Chat Room> \n')
		print("List of connected Friends")
		if cmd == 'list':
			list_connections(cmd)
		elif 'select' in cmd:
			conn = get_target(cmd)
			if conn is not None:
				send_to_target_client(conn)
	
	
	
	
	
		
init(address)
start_chat()
