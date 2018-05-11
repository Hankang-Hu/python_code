from twisted.internet import protocol,reactor

HOST = 'localhost'
PORT = 4002

class TCliProtocol(protocol.Protocol):
	def sendData(self):
		data = input('input the message:')
		if data:
			print('sending:',data)
