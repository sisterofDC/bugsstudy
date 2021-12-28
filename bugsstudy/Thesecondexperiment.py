import socket
import os
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9527))
remoteHost=''
remotePort=0
event = threading.Event()

def recv(name):
    print(os.getpid(), name)
    global remoteHost,remotePort
    while True:
        revcData, (remoteHost, remotePort) = sock.recvfrom(1024)
        event.set()
        print("[%s:%s] connect" % (remoteHost, remotePort), revcData)  # 接收客户端的ip, port

def send(name):
    print(os.getpid(), name)
    event.wait()
    while True:
        print((remoteHost, remotePort))
        data = input()
        sock.sendto(data.encode('utf-8'), (remoteHost, remotePort))


if __name__ == '__main__':
    recv_msg = threading.Thread(target=recv, args=("recv_msg",))
    send_msg = threading.Thread(target=send, args=("send_msg",))
    recv_msg.start()
    send_msg.start()