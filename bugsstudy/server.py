import socket
import ssl

class Server(object):
    def udpServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', 9527))
        while True:
            revcData, (remoteHost, remotePort) = sock.recvfrom(1024)
            print("[%s:%s] connect" % (remoteHost, remotePort), revcData)  # 接收客户端的ip, port
            data = input()
            if data == '0':
                break
            sock.sendto(data.encode('utf-8'), (remoteHost, remotePort))
        sock.close()

    def tcpServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 8090))
        sock.listen(5)
        conn, addr = sock.accept()
        while True:
            revcData = conn.recv(1024)
            print(revcData, addr)
            data = input()
            conn.send(data.encode('utf-8'))
            if data == '0':
                break
        sock.close()

    def httpreqest(self):
        s = ssl.wrap_socket(socket.socket())
        s.connect(('www.bing.com', 443))
        s.send(b'GET / HTTP/1.1\r\nHost: www.bing.com\r\nConnection: close\r\n\r\n')
        # GET / article - types / 6 / HTTP / 1.1
        # Host: www.zhangdongshengtech.com
        # Connection: close
        buffer = []
        while True:
            d = s.recv(1024)
            if d:
                buffer.append(d)
            else:
                break
        data = b''.join(buffer)
        s.close()
        header, html = data.split(b'\r\n\r\n', 1)
        print(header.decode('utf-8'))
        with open('../savehtml/save.html','wb') as f:
            f.write(html)


if __name__ == "__main__":
    udpServer = Server()
    udpServer.httpreqest()
