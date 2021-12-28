import socket


class UdpClient(object):
    def tcpclient(self):
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            data = input()
            clientSock.sendto(data.encode('utf-8'), ('localhost', 9527))
            recvData = clientSock.recvfrom(1024)
            print(recvData)
            if data == '0':
                break
        clientSock.close()


if __name__ == "__main__":
    udpClient = UdpClient()
    udpClient.tcpclient()
