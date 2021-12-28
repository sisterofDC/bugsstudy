import socket

s_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '0.0.0.0'
port = 8080
address = (host, port)


def recv_meg():
    s_UDP.bind(address=address)
    while True:
        data = s_UDP.recvfrom(bufsize=1024)
        print(data)


if __name__ == '__main__':
    recv_meg()
