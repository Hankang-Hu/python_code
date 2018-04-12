
from socket import *
from time import ctime

HOST = ''
PORT = 40005
BUFFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSocket = socket(AF_INET,SOCK_STREAM)
tcpSerSocket.bind(ADDR)
tcpSerSocket.listen(5)

while True:
    print('waiting for connection..')
    tcpCliSocket,addr=tcpSerSocket.accept()
    print('...connected from:',addr)

    while True:
        data = bytes.decode(tcpCliSocket.recv(BUFFSIZE))
        if not data:
            break
        print(data)
        data = data + ctime()
        tcpCliSocket.send(str.encode(data))
    tcpCliSocket.close
tcpSerSocket.close
