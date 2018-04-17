from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 4000
ADDR=(HOST,PORT)

class MyRequestHandler(SRH):
	def handle(self):
		print('...connected from :',self.client_address)
		data = '[%s] : %s' %(ctime(),bytes.decode(self.rfile.readline()))
		print(data.strip())
		self.wfile.write(str.encode(data))

tcpServ = TCP(ADDR,MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()
