from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('> ')
        if data:
            print('...sending %r...' % data)
            self.transport.write(data.encode())
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode())
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()


if __name__ == '__main__':
    reactor.connectTCP(HOST, PORT, TSClntFactory())
    reactor.run()
