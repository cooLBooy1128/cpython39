import socket

HOST = 'localhost'
PORT = 8000
ADDR = (HOST, PORT)
BUFSIZ = 1024


def main():
    while True:
        tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        data = input('> ')
        if not data:
            break
        tcpCliSock.send(b'%s\r\n' % data.encode())
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data.strip().decode())
        tcpCliSock.close()


if __name__ == '__main__':
    main()
