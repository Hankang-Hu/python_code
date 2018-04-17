from socket import *

HOST = 'localhost'
PORT = 4001
BUFFSIZE = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
	data = input('input the message:')
	if not data:
		break
	udpCliSock.sendto(str.encode(data),ADDR)
	data,ADDR = udpCliSock.recvfrom(BUFFSIZE)
	if not data:
		break
	data = bytes.decode(data)
	print(data.strip())
