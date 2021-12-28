import socket


class UdpServer(object):
    def tcpServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', 9527))  # 绑定同一个域名下的所有机器
        while True:
            revcData, (remoteHost, remotePort) = sock.recvfrom(1024)
            print("[%s:%s] connect" % (remoteHost, remotePort),revcData)  # 接收客户端的ip, port
            data = input()
            if data == '0':
                break
            sock.sendto(data.encode('utf-8'), (remoteHost, remotePort))
        sock.close()


if __name__ == "__main__":
    udpServer = UdpServer()
    udpServer.tcpServer()