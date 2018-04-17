from socket import *
from time import ctime

HOST = ''
PORT = 4001
BUFFSIZE = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print('waiting for message...')
	data,addr = udpSerSock.recvfrom(BUFFSIZE)
	if not data:
		break
	data = bytes.decode(data)
	data = ctime() + ':\t' + data
	udpSerSock.sendto(str.encode(data),addr)
	print('received from  and send to:',addr)
udpSerSock.close()
