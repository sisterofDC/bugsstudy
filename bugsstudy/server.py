import socket

# UDP
s_UDP = socket.socket(socket.AF_IRDA, socket.SOCK_DGRAM)
host = '0.0.0.0'
port = 8080
address = (host, port)


def send_meg():
    while True:
        data = input()
        if data == '0':
            break
        s_UDP.sendto(data=data.encode("utf-8"), address=('0.0.0.0', 8080))
    s_UDP.close()


if __name__ == '__main__':
    send_meg()
