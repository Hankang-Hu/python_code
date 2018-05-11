from twisted.internet import protocol,reactor
from time import ctime

PORT = 4002

class TSserProtocol(protocol.Protocol):
	def connectionMade(self):
		clnt = self.clnt = self.transport.getPeer().host
		print('connected from:',clnt)
	def dataReceived(self,data):
		data = ('[%s]:  %s'%(ctime(),data))
		self.transport.write(str.encode(data))
factory = protocol.Factory()
factory.protocol = TSserProtocol
print('waiting for connection...')
reactor.listenTCP(PORT,factory)
reactor.run()
