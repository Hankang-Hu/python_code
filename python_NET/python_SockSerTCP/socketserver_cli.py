from socket import *

HOST = 'localhost'
PORT = 4000
BUFFSIZE = 1024
ADDR = (HOST,PORT)

while True:
	tcpCliSock = socket(AF_INET,SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	data = input('input the massage:')
	if not data:
		break
	tcpCliSock.send(str.encode('%s\r\n' % data))
	data = tcpCliSock.recv(BUFFSIZE)
	if not data:
		break
	data = bytes.decode(data)
	print(type(data))
	print(data.strip())
	tcpCliSock.close()
