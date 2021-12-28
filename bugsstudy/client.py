import socket


class Client(object):
    def udpclient(self):
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            data = input()
            clientSock.sendto(data.encode('utf-8'), ('localhost', 9527))
            recvData = clientSock.recvfrom(1024)
            print(recvData)
            if data == '0':
                break
        clientSock.close()

    def tcpclient(self):
        clientsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientsock.connect(('localhost',8090))
        while True:
            data = input()
            clientsock.send(data.encode('utf-8'))
            recvData = clientsock.recv(1024)
            print(recvData)
            if data == '0':
                break
        clientsock.close()


if __name__ == "__main__":
    udpClient = Client()
    udpClient.udpclient()
