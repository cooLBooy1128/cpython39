from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.transport.getPeer()
        print('...connected from:', clnt)

    def dataReceived(self, data):
        self.transport.write(b'[%s] %s' % (ctime().encode(), data))


if __name__ == '__main__':
    factory = protocol.Factory()
    factory.protocol = TSServProtocol
    print('waiting for connection...')
    reactor.listenTCP(PORT, factory)
    reactor.run()
