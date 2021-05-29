import socketserver
from time import ctime

HOST = ''
PORT = 8000
ADDR = (HOST, PORT)


class MyRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print('...connected from:', self.client_address)
        data = self.rfile.readline()
        print(data)
        self.wfile.write(b'[%s] %s' % (ctime().encode(), data))


if __name__ == '__main__':
    tcpServ = socketserver.TCPServer(ADDR, MyRequestHandler)
    print('waiting for connection...')
    tcpServ.serve_forever()
