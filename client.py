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
	global Friends_list
	sock.send(str.encode(cmd))
	Friends_list=sock.recv(1024)
	Friends_list=eval(Friends_list.decode("utf-8"))
	for i,x in enumerate(Friends_list):
		print(i," ",x)
def chat_with_ur_friend(addr):
	while True:
		
		sock.send(bytes(input(""),'utf-8'))
		data=sock.recv(1024)
		print(data)
	
	






def req_to_target_client(addr):
	try:
		print("entered")
		print(addr)
		sock.send(str.encode(str(addr)))
		addr=sock.recv(1024)
		addr=eval(addr.decode("utf-8"))
		print(type(addr[0]))
		print(type(addr[1]))

		chat_with_ur_friend(addr)
	except:
		print("exception in targetclient")
	

def start_chat():

	while True:
		cmd = input('Chat Room> \n')
		print("List of connected Friends")
		if cmd == 'list':
			list_connections(cmd)
		elif 'select' in cmd:
			cmd=cmd.split()
			addr = Friends_list[int(cmd[1])]
			if addr is not None:
				req_to_target_client(addr)
	
	
	
	
	
		
init(address)
start_chat()
