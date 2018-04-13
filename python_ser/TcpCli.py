from socket import *

HOST = '127.0.0.1'
PORT = 40005
BUFFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSocket = socket(AF_INET,SOCK_STREAM)
tcpCliSocket.connect(ADDR)

while True:
    data = input('input the massage:')
    if not data:
        break
    tcpCliSocket.send(str.encode(data))
    data = tcpCliSocket.recv(BUFFSIZE)
    if not data:
        break
    print(data)
tcpCliSocket.close()
